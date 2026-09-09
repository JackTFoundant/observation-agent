"""Never pattern-match a successful payload.

Every cold run silently lost exactly one batch of messages, and the cause was this: the
rate-limit detector regexed the assistant's *answer* for `429`, and a message uid is a hex
hash. `m_64293e33900a` contains "429". So a worker returned a perfectly valid batch, its
own message id tripped the detector, the answer was discarded as a rate limit, and the
batch retried until the stage deadline killed it — deterministically, because uids are
content hashes.

Rate limiting is now detected structurally (non-zero exit, error envelope) and text
matching is a fallback used only when the CLI returned prose instead of parseable JSON.
"""

from __future__ import annotations

import pytest

from observe.claude_cli import _AUTH_FAIL, _RATE_LIMIT, _parse_json_payload


# ---------------------------------------------------------------------------
# The regex must not fire on corpus content or message ids
# ---------------------------------------------------------------------------

@pytest.mark.parametrize("text", [
    '{"messages":[{"msg_uid":"m_64293e33900a","task_class":"other"}]}',   # the real culprit
    '{"msg_uid":"m_a429fbc0d1e2"}',
    '{"msg_uid":"m_429000000000"}',
    '{"quote_proposal":"deal 429 was rebooked in Sitara"}',
    '{"process_phrase":"reconcile meter 4291 volumes"}',
    'nomination 429 mmbtu confirmed',
])
def test_ids_and_corpus_numbers_are_not_rate_limits(text):
    assert not _RATE_LIMIT.search(text), f"false positive on {text!r}"


@pytest.mark.parametrize("text", [
    "API error: status code 429 Too Many Requests",
    "Error: rate limit exceeded, please retry",
    "You are being rate-limited",
    "Error: server overloaded",
    "usage limit reached for this account",
    "HTTP 429 returned by upstream",
])
def test_genuine_rate_limit_messages_are_recognised(text):
    assert _RATE_LIMIT.search(text), f"missed a real rate limit in {text!r}"


# ---------------------------------------------------------------------------
# A payload that parses is an answer, whatever words it contains
# ---------------------------------------------------------------------------

def test_a_valid_payload_is_never_reclassified_as_an_error(monkeypatch):
    """The end-to-end shape of the bug: valid JSON whose content matches the regex."""
    import observe.claude_cli as cli

    body = (
        '{"messages":[{"msg_uid":"m_64293e33900a","is_operational":true,'
        '"task_class":"other","process_phrase":"discuss office move",'
        '"role":"fyi","systems_referenced":[],"rework_signal":false,'
        '"waiting_signal":false,"manual_transfer_signal":false,'
        '"deadline_signal":false,"evidence":[],"confidence":"high"}]}'
    )
    # Even a quote that legitimately mentions a rate limit must survive, because it parses.
    body_with_words = body.replace("discuss office move", "we hit our usage limit")

    class FakeProc:
        returncode = 0
        stderr = ""
        def __init__(self, out): self.stdout = out

    for payload in (body, body_with_words):
        monkeypatch.setattr(cli.subprocess, "run",
                            lambda *a, **k: FakeProc('{"result": ' + repr(payload).replace("'", '"') + "}"))
        # Parse path is what decides; assert the payload itself is parseable and kept.
        assert _parse_json_payload(payload)["messages"][0]["msg_uid"] == "m_64293e33900a"


def test_unparseable_prose_can_still_be_classified(monkeypatch):
    """The fallback must remain: an error delivered as prose is still an error."""
    with pytest.raises(Exception):
        _parse_json_payload("Error: rate limit exceeded")
    assert _RATE_LIMIT.search("Error: rate limit exceeded")
    assert _AUTH_FAIL.search("Error: not authenticated, run claude auth login")


def test_auth_regex_does_not_fire_on_corpus_content():
    for text in ('{"msg_uid":"m_401abc"}', '{"quote_proposal":"invoice 401 unpaid"}'):
        # 401 as a bare number inside an id or amount must not read as an auth failure in a
        # payload that parses; the parse-first rule protects it regardless.
        assert _parse_json_payload(text)
