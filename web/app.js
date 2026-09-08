/* Dashboard client. Vanilla ES modules, no framework, no build step.
 *
 * The one piece that carries real weight is `showRaw`: it fetches the corpus file as an
 * ArrayBuffer and highlights the citation by *slicing at the published byte offsets*
 * rather than by searching for the stored quote. If an offset were wrong, the highlight
 * would visibly land in the wrong place — which is the point. The picture cannot be
 * prettier than the data.
 */

const $ = (sel, el = document) => el.querySelector(sel);
const money = (v) => '$' + Math.round(v).toLocaleString('en-US');
const money2 = (v) => '$' + v.toLocaleString('en-US', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
const esc = (s) => String(s ?? '').replace(/[&<>"']/g, (c) =>
  ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));

const state = { summary: null, method: null, opps: new Map(), artifacts: null, quarantine: null, residual: null };

async function getJSON(url) {
  const r = await fetch(url);
  if (!r.ok) throw new Error(`${url} -> ${r.status}`);
  return r.json();
}

/* ---------------- shell ---------------- */

async function boot() {
  try {
    state.summary = await getJSON('/api/summary');
  } catch (e) {
    $('#view').innerHTML = `<div class="wrap"><div class="banner">No report found. Run
      <code>make run</code> first, then reload.</div></div>`;
    return;
  }
  $('#scope').textContent = state.summary.scope_line;
  $('#runmeta').innerHTML = `run ${esc(state.summary.run_id)}<br>corpus ${esc(state.summary.corpus_digest.slice(0, 12))}`;
  paintVerifyBadge();
  window.addEventListener('hashchange', route);
  $('#drawerClose').onclick = closeDrawer;
  $('#backdrop').onclick = closeDrawer;
  document.addEventListener('keydown', (e) => { if (e.key === 'Escape') closeDrawer(); });
  route();
}

async function paintVerifyBadge() {
  const badge = $('#verifyBadge');
  try {
    const v = await getJSON('/api/verify');
    if (v.passed) {
      badge.className = 'badge pass';
      badge.textContent = `verified · ${v.checks} checks`;
      badge.title = 'Every citation re-anchored and every number recomputed from scratch';
    } else {
      badge.className = 'badge fail';
      badge.textContent = `${v.failures.length} verification failures`;
    }
  } catch {
    badge.className = 'badge warn';
    badge.textContent = 'unverified — run make verify';
    document.documentElement.style.setProperty('--ink', '#3d4045');
  }
}

function route() {
  const hash = location.hash.replace(/^#/, '') || '/';
  document.querySelectorAll('nav a').forEach((a) => {
    a.classList.toggle('active', a.dataset.route === hash.split('/').slice(0, 2).join('/'));
  });
  if (hash.startsWith('/opp/')) return viewOpportunity(hash.slice(5));
  if (hash === '/artifacts') return viewArtifacts();
  if (hash === '/excluded') return viewExcluded();
  if (hash === '/method') return viewMethod();
  return viewOverview();
}

function render(html) { $('#view').innerHTML = `<div class="wrap">${html}</div>`; }

/* ---------------- overview ---------------- */

function viewOverview() {
  const s = state.summary;
  const d = s.headline.dollars_per_month;
  const h = s.headline.automatable_hours_per_month;
  const att = s.attribution;
  const counted = s.opportunities.filter((o) => o.status === 'counted');
  const max = Math.max(...counted.map((o) => o.dollars_per_month.high), 1);

  render(`
    <section class="hero">
      <div class="hero-label">Recoverable, per month</div>
      <button class="hero-figure" id="heroBtn" title="How this number was reached">${money(d.base)}</button>
      <div class="hero-range">range ${money(d.low)} &ndash; ${money(d.high)}</div>
      <div class="hero-sub">
        ${h.base.toFixed(0)} automatable hours a month at a blended $85/hour, across
        ${counted.length} evidenced opportunities.
        ${s.evidence.citations_verified} citations, each anchored to an exact byte range in a
        raw file.
      </div>
      <div class="hero-note">
        <strong>This is a floor, not a total.</strong>
        ${att.attributed_to_counted_opportunities.toLocaleString()} of
        ${att.operational_messages.toLocaleString()} operational messages
        (${(att.share_attributed * 100).toFixed(0)}%) could be attributed to an identified
        recurring process. The rest is a long tail that failed the promotion gate and is
        deliberately left uncosted. The counts here are measured; the minutes-per-task are
        estimates nobody could verify, which is why the range is shown as prominently as the
        number. <a href="#/method">See the assumptions</a>.
      </div>
    </section>

    <h2 class="section">Ranked opportunities</h2>
    <table class="ranked">
      <thead><tr>
        <th></th><th>Opportunity</th>
        <th class="num">$ / month</th><th class="hide-sm">Range</th>
        <th class="num hide-sm">Hrs</th><th class="num hide-sm">Inst.</th>
        <th class="num hide-sm">Mo.</th><th class="num">Cites</th><th>Conf.</th>
      </tr></thead>
      <tbody>
        ${counted.map((o, i) => rowHTML(o, i + 1, max)).join('')}
      </tbody>
    </table>

    <h2 class="section">By value</h2>
    <div class="chart">
      ${counted.slice(0, 10).map((o) => `
        <div class="chart-row">
          <div class="chart-label" title="${esc(o.title)}">${esc(o.title)}</div>
          <div class="chart-track"><div class="chart-fill" style="width:${(o.dollars_per_month.base / max * 100).toFixed(1)}%"></div></div>
          <div class="chart-val">${money(o.dollars_per_month.base)}</div>
        </div>`).join('')}
    </div>

    ${notCountedHTML(s)}
  `);

  $('#heroBtn').onclick = () => showHeroMath();
  document.querySelectorAll('[data-opp]').forEach((el) => {
    el.onclick = (e) => { e.preventDefault(); location.hash = `#/opp/${el.dataset.opp}`; };
  });
}

function rowHTML(o, rank, max) {
  const d = o.dollars_per_month;
  const lo = (d.low / max) * 100, hi = (d.high / max) * 100, base = (d.base / max) * 100;
  const src = o.source === 'header_frequency'
    ? '<span class="chip header" title="Found deterministically from subject lines, with no model involved">headers</span>' : '';
  return `<tr>
    <td class="rank">${rank}</td>
    <td>
      <button class="opp-link" data-opp="${esc(o.opportunity_id)}">${esc(o.title)}</button>
      <div class="opp-meta">${esc(o.task_class.replace(/_/g, ' '))} ${src}
        ${o.flags.includes('artifact_below_threshold_included_on_judgment') ? '<span class="chip low">artifact on judgment</span>' : ''}
      </div>
    </td>
    <td class="num money">${money(d.base)}
      <div class="rangebar"><i style="left:${lo}%;width:${Math.max(hi - lo, 1)}%"></i><b style="left:${base}%"></b></div>
    </td>
    <td class="hide-sm range-txt">${money(d.low)}&ndash;${money(d.high)}</td>
    <td class="num hide-sm">${o.automatable_hours_per_month.base.toFixed(1)}</td>
    <td class="num hide-sm">${o.instances}</td>
    <td class="num hide-sm">${o.months}</td>
    <td class="num">${o.citations}</td>
    <td><span class="chip ${o.confidence}">${o.confidence}</span></td>
  </tr>`;
}

function notCountedHTML(s) {
  const nc = s.not_counted;
  if (!nc.low_confidence.count && !nc.quarantined.count) return '';
  return `
    <h2 class="section">Not counted</h2>
    <p class="note">
      ${nc.quarantined.count} opportunit${nc.quarantined.count === 1 ? 'y was' : 'ies were'}
      quarantined for insufficient evidence
      (<span class="strike">${money(nc.quarantined.dollars_per_month_base)}</span>/month excluded)
      and ${nc.low_confidence.count} demoted to low confidence
      (<span class="strike">${money(nc.low_confidence.dollars_per_month_base)}</span>/month
      excluded from the headline). Nothing was deleted &mdash;
      <a href="#/excluded">see every exclusion and its reason</a>.
    </p>`;
}

/* ---------------- opportunity ---------------- */

async function viewOpportunity(id) {
  render('<div class="loading">Loading…</div>');
  let o = state.opps.get(id);
  if (!o) { o = await getJSON(`/api/opportunity/${encodeURIComponent(id)}`); state.opps.set(id, o); }

  const d = o.dollars_per_month, dv = o.derivation, m = dv.measured, a = dv.assumed;
  const n = o.narrative || {};
  const arts = (state.summary.artifacts || []).filter((x) => x.opportunity_id === id);

  render(`
    <div class="detail">
      <a href="#/" style="font-size:13px;color:var(--ink-soft)">&larr; all opportunities</a>
      <h1 style="margin-top:14px">${esc(o.title)}</h1>
      <div class="kicker">
        ${esc(o.task_class.replace(/_/g, ' '))} ·
        ${o.source === 'header_frequency' ? 'discovered from subject lines, no model involved' : 'discovered by clustering message content'} ·
        confidence ${esc(o.confidence)} ·
        <code>${esc(o.opportunity_id)}</code>
      </div>

      <div class="figrow">
        <div class="fig"><div class="fig-label">Per month</div>
          <div class="fig-value">${money(d.base)}</div>
          <div class="fig-sub">${money(d.low)} &ndash; ${money(d.high)}</div></div>
        <div class="fig"><div class="fig-label">Automatable hours</div>
          <div class="fig-value">${o.automatable_hours_per_month.base.toFixed(1)}</div>
          <div class="fig-sub">of ${o.hours_per_month.base.toFixed(1)} total</div></div>
        <div class="fig"><div class="fig-label">Task instances</div>
          <div class="fig-value">${m.instances}</div>
          <div class="fig-sub">${m.messages} messages</div></div>
        <div class="fig"><div class="fig-label">Spread</div>
          <div class="fig-value">${o.months.length}</div>
          <div class="fig-sub">months · ${o.people} people</div></div>
        <div class="fig"><div class="fig-label">Evidence</div>
          <div class="fig-value">${o.citations.length}</div>
          <div class="fig-sub">verified citations</div></div>
      </div>

      ${o.status !== 'counted' ? `<div class="banner"><strong>Not counted.</strong>
        ${esc(o.status_reason)} This opportunity is excluded from every dollar total.</div>` : ''}
      ${n.discovery_note ? `<div class="banner info">${esc(n.discovery_note)}</div>` : ''}

      <div class="prose">
        ${n.what_happens ? `<h3>What happens</h3><p>${esc(n.what_happens)}</p>` : ''}
        ${n.where_it_stalls ? `<h3>Where it stalls</h3><p>${esc(n.where_it_stalls)}</p>` : ''}
        ${n.why_it_recurs ? `<h3>Why it recurs</h3><p>${esc(n.why_it_recurs)}</p>` : ''}
        ${n.automation_opportunity ? `<h3>What could absorb it</h3><p>${esc(n.automation_opportunity)}</p>` : ''}
      </div>

      <h2 class="section">How the number was reached</h2>
      <div class="derivation">
        <div class="measured"><h4>Measured from the corpus</h4><dl>
          ${dlRows({
            'task instances': m.instances, 'messages': m.messages,
            'touches per instance': (m.messages / Math.max(m.instances, 1)).toFixed(2),
            'median participants': m.participants_median,
            'months of coverage': m.months, 'distinct senders': m.senders,
            'rework rate': pct(m.rework_rate), 'waiting rate': pct(m.waiting_rate),
            'dated / undated': `${m.dated_messages} / ${m.undated_messages}`,
          })}
        </dl></div>
        <div class="assumed"><h4>Assumed — not measured</h4><dl>
          ${dlRows({
            'handle min': a.handle_min, 'per touch min': a.per_touch_min,
            'rework min': a.rework_min, 'waiting admin min': a.waiting_admin_min,
            'automatable share': a.automatable_share,
            'coordination alpha': dv.assumed_global.coordination_alpha,
            'blended rate': '$' + dv.assumed_global.blended_rate_usd_per_hour + '/h',
          })}
        </dl>
        <div style="margin-top:10px;font-size:12px;color:var(--ink-faint)">
          from <code>${esc(dv.assumption_source)}</code></div>
        </div>
      </div>
      <pre class="steps">${dv.steps.map(esc).join('\n')}</pre>
      <p class="note" style="margin-top:10px">
        <code>make verify</code> recomputes ${money2(dv.result.dollars_per_month)} from these
        inputs alone and asserts it matches to the cent.
      </p>

      ${arts.length ? `<h2 class="section">Ready for Monday morning</h2>
        ${arts.map((x) => `<div class="artifact-card">
          <h3>${esc(x.title)}</h3>
          <div class="meta">${esc(x.artifact_type)} · <code>${esc(x.filename)}</code> · ${esc(x.review_status)}</div>
          <button class="copybtn" data-art="${esc(x.filename)}">Read it</button>
        </div>`).join('')}` : ''}

      <h2 class="section">Evidence</h2>
      <p class="note" style="margin-bottom:14px">
        Every quote below was sliced out of the file named beneath it. Click one to see it
        highlighted in the raw message at those exact byte offsets.
      </p>
      ${o.citations.map(citeHTML).join('')}
      ${(o.quarantined_citations || []).length ? `
        <h2 class="section">Evidence withheld</h2>
        ${o.quarantined_citations.map((q) => `<div class="cite dim">
          <blockquote>${esc(q.proposal_preview)}</blockquote>
          <div class="cite-meta">withheld — <strong>${esc(q.reason)}</strong>
            ${q.detail ? '· ' + esc(q.detail) : ''} · ${esc(q.source_path)}</div>
        </div>`).join('')}` : ''}
    </div>
  `);

  document.querySelectorAll('[data-cite]').forEach((el) => {
    el.onclick = () => showRaw(o, el.dataset.cite);
  });
  document.querySelectorAll('[data-art]').forEach((el) => {
    el.onclick = () => showArtifact(el.dataset.art);
  });
}

const pct = (v) => (v * 100).toFixed(0) + '%';
function dlRows(obj) {
  return Object.entries(obj).map(([k, v]) => `<dt>${esc(k)}</dt><dd>${esc(v)}</dd>`).join('');
}

function citeHTML(c) {
  const weak = !['raw_exact', 'decoded_exact', 'rewrapped'].includes(c.match_tier);
  return `<div class="cite ${weak ? 'weak' : ''}">
    <blockquote>${esc(c.quote.trim())}</blockquote>
    <div class="cite-meta">
      <button data-cite="${esc(c.citation_id)}">${esc(c.source_path)}</button>
      · bytes ${c.raw_start}&ndash;${c.raw_end} · lines ${c.line_start}&ndash;${c.line_end}
      ${c.sent_at ? '· ' + esc(c.sent_at.slice(0, 10)) : ''}
      ${c.sender ? '· ' + esc(c.sender) : ''}
      <span class="tierchip ${weak ? 'weak' : ''}">${esc(c.match_tier)}</span>
      ${c.repaired ? '<span class="tierchip weak">normalized to source text</span>' : ''}
    </div>
  </div>`;
}

/* ---------------- the raw message view ---------------- */

async function showRaw(opp, citationId) {
  const c = opp.citations.find((x) => x.citation_id === citationId);
  if (!c) return;
  openDrawer(`<h2>${esc(c.subject || '(no subject)')}</h2>
    <div class="sub">${esc(c.source_path)} · loading bytes…</div>`);

  const res = await fetch('/raw/' + c.source_path.split('/').map(encodeURIComponent).join('/'));
  const buf = await res.arrayBuffer();
  const sha = res.headers.get('X-Sha256') || '';
  const bytes = new Uint8Array(buf);

  // Slice at the PUBLISHED offsets. Not a string search: if the offsets were wrong, the
  // highlight would land in the wrong place, visibly.
  const dec = new TextDecoder('iso-8859-1');
  const WINDOW = 20000;
  const from = Math.max(0, c.raw_start - WINDOW);
  const to = Math.min(bytes.length, c.raw_end + WINDOW);
  const before = dec.decode(bytes.slice(from, c.raw_start));
  const hit = dec.decode(bytes.slice(c.raw_start, c.raw_end));
  const after = dec.decode(bytes.slice(c.raw_end, to));
  const truncated = from > 0 || to < bytes.length;

  const shaOK = sha && c.source_sha256 && sha === c.source_sha256;
  const weak = !['raw_exact', 'decoded_exact', 'rewrapped'].includes(c.match_tier);

  openDrawer(`
    <h2>${esc(c.subject || '(no subject)')}</h2>
    <div class="sub">${esc(c.source_path)} ·
      ${c.sent_at ? esc(c.sent_at.slice(0, 19)) : 'undated'} ·
      from ${esc(c.sender || 'unknown')}</div>

    ${shaOK ? `<div class="banner info">The file on disk still hashes to
      <code>${esc(sha.slice(0, 16))}</code>, matching what the report recorded. The highlight
      below is produced by slicing this file at bytes ${c.raw_start}&ndash;${c.raw_end} — not
      by searching for the quote.</div>`
      : `<div class="banner">The file's hash does not match what the report recorded. The
      corpus may have changed since the run.</div>`}

    ${c.match_tier === 'decoded_exact' ? `<div class="banner">This quote is verbatim in the
      quoted-printable-<em>decoded</em> body. The raw bytes shown differ only by <code>=20</code>
      style soft-encodings and soft line breaks.</div>` : ''}
    ${c.match_tier === 'rewrapped' ? `<div class="banner">This quote matched after collapsing
      whitespace only: the characters are identical, but the mail client hard-wrapped the line
      so it cannot be found byte-for-byte on one line.</div>` : ''}
    ${weak ? `<div class="banner">Weaker evidence: this quote matched only after case and
      punctuation folding, so it is not character-identical to the source.</div>` : ''}
    ${c.repaired ? `<div class="banner">The proposed quote was a paraphrase. It was discarded
      and the closest actual text from the file was used instead — what you see below is the
      file's own wording.</div>` : ''}

    <div class="rawhead">
      <span>bytes ${c.raw_start}&ndash;${c.raw_end}</span>
      <span>lines ${c.line_start}&ndash;${c.line_end}</span>
      <span>file ${bytes.length.toLocaleString()} bytes</span>
      <button class="copybtn" data-copy="${esc(c.check_commands.dd)}">copy dd</button>
      <button class="copybtn" data-copy="${esc(c.check_commands.sed)}">copy sed</button>
      <a href="/raw/${c.source_path}?slice=${c.raw_start}-${c.raw_end}" target="_blank"
         style="color:var(--accent)">open the byte range</a>
    </div>
    ${truncated ? `<div class="banner">Showing a ${((to - from) / 1000).toFixed(0)} KB window
      around the citation; this file is ${(bytes.length / 1000).toFixed(0)} KB.
      <a href="/raw/${c.source_path}" target="_blank">open the whole file</a>.</div>` : ''}
    <pre class="raw">${esc(before)}<mark id="hit">${esc(hit)}</mark>${esc(after)}</pre>
  `);

  document.querySelectorAll('[data-copy]').forEach((b) => {
    b.onclick = async () => {
      await navigator.clipboard.writeText(b.dataset.copy);
      const t = b.textContent; b.textContent = 'copied'; setTimeout(() => (b.textContent = t), 1200);
    };
  });
  const hitEl = $('#hit');
  if (hitEl) hitEl.scrollIntoView({ block: 'center' });
}

/* ---------------- other views ---------------- */

async function showHeroMath() {
  const s = state.summary;
  const counted = s.opportunities.filter((o) => o.status === 'counted');
  openDrawer(`
    <h2>How the headline is built</h2>
    <div class="sub">summed unrounded, quantized once, half-even</div>
    <p class="note">Only opportunities with enough verified evidence to be
    <em>counted</em> contribute. Each line links to its own derivation.</p>
    <table class="assump"><thead><tr><th>Opportunity</th><th class="num">$ / month</th></tr></thead>
    <tbody>
      ${counted.map((o) => `<tr><td><a href="#/opp/${esc(o.opportunity_id)}"
        style="color:var(--accent)">${esc(o.title)}</a></td>
        <td class="num">${money2(o.dollars_per_month.base)}</td></tr>`).join('')}
      <tr><td><strong>Total</strong></td>
        <td class="num"><strong>${money2(s.headline.dollars_per_month.base)}</strong></td></tr>
    </tbody></table>
    <p class="note" style="margin-top:16px">
      <code>make verify</code> asserts this total equals the sum of the parts, and recomputes
      each part from its own published derivation.</p>
  `);
  $('#drawer').querySelectorAll('a[href^="#/"]').forEach((a) => { a.onclick = closeDrawer; });
}

async function viewArtifacts() {
  render('<div class="loading">Loading…</div>');
  let list = [];
  try { list = await getJSON('/api/artifacts'); } catch { list = []; }
  render(`
    <h2 class="section">Ready for Monday morning</h2>
    <p class="note" style="margin-bottom:20px">
      Drafted for the opportunities above the threshold in
      <code>config/thresholds.yml</code>. Every sentence describing current practice carries a
      citation id that resolves to verified evidence; recommendations carry no citation and sit
      under their own heading, so observation never blurs into proposal. All are unreviewed
      drafts and say so.
    </p>
    ${list.length ? list.map((a) => `<div class="artifact-card">
      <h3>${esc(a.title)}</h3>
      <div class="meta">${esc(a.artifact_id)} · ${esc(a.artifact_type)} ·
        ${a.evidence.length} citations · ${esc(a.review_status)}
        ${a.below_threshold_judgment_call ? ' · <span class="chip low">below threshold, included on judgment</span>' : ''}</div>
      <div style="font-size:13px;color:var(--ink-soft);margin-bottom:10px">
        for <a href="#/opp/${esc(a.opportunity_id)}" style="color:var(--accent)">${esc(a.opportunity_title)}</a></div>
      <button class="copybtn" data-art="${esc(a.filename)}">Read it</button>
    </div>`).join('') : '<p class="note">No artifacts met the threshold on this run.</p>'}
  `);
  document.querySelectorAll('[data-art]').forEach((el) => {
    el.onclick = () => showArtifact(el.dataset.art);
  });
}

async function showArtifact(filename) {
  const res = await fetch('/api/artifact/' + encodeURIComponent(filename));
  const text = await res.text();
  openDrawer(`<h2>${esc(filename)}</h2>
    <div class="sub">plain Markdown at <code>out/artifacts/${esc(filename)}</code></div>
    <pre class="md">${esc(text)}</pre>`);
}

async function viewExcluded() {
  render('<div class="loading">Loading…</div>');
  const [q, r] = await Promise.all([getJSON('/api/quarantine'), getJSON('/api/residual')]);
  render(`
    <h2 class="section">Not counted</h2>
    <p class="note">${esc(q.explanation)}</p>
    ${q.opportunities.length ? q.opportunities.map((o) => `<div class="excluded-row">
      <strong>${esc(o.title)}</strong>
      <span class="strike" style="margin-left:8px">${money(o.would_have_been_dollars_per_month)}/month</span>
      <div class="why">${esc(o.status)} — ${esc(o.reason)}</div>
      <div style="font-size:12.5px;color:var(--ink-faint)">${o.verified_citations} verified citations · <code>${esc(o.opportunity_id)}</code></div>
    </div>`).join('') : '<p class="note">No opportunities were excluded on this run.</p>'}

    ${q.citations.length ? `<h2 class="section">Citations rejected</h2>
      <p class="note">Quotes a model proposed that could not be tied to bytes in the file it
      named. They were discarded, not repaired into something plausible.</p>
      ${q.citations.map((c) => `<div class="excluded-row">
        <div style="font-family:var(--serif);font-size:15px">${esc(c.proposal_preview)}</div>
        <div class="why">${esc(c.reason)}${c.detail ? ' — ' + esc(c.detail) : ''}</div>
        <div style="font-size:12.5px;color:var(--ink-faint)">${esc(c.source_path)}</div>
      </div>`).join('')}` : ''}

    <h2 class="section">Candidates declined</h2>
    <p class="note">${esc(r.explanation)}</p>
    <p class="note" style="margin-top:10px">
      ${r.content_clusters.length} content clusters of 3+ messages and
      ${r.recurring_series.length} recurring subject series were found and not promoted.
      A few of the largest:
    </p>
    ${r.content_clusters.slice(0, 14).map((c) => `<div class="excluded-row">
      <strong>${esc(c.label)}</strong>
      <span style="color:var(--ink-faint);margin-left:8px">${c.messages} messages</span>
      <div class="why">${esc(c.failed_gates.join('; '))}</div>
    </div>`).join('')}
    ${r.recurring_series.slice(0, 10).map((s) => `<div class="excluded-row">
      <strong>“${esc(s.example_subject)}”</strong>
      <span style="color:var(--ink-faint);margin-left:8px">${s.instances}&times; ${esc(s.cadence)}</span>
      <div class="why">${esc((s.failed_gates || []).join('; '))}</div>
    </div>`).join('')}
  `);
}

async function viewMethod() {
  render('<div class="loading">Loading…</div>');
  const m = await getJSON('/api/method');
  const s = state.summary;
  const tc = m.assumptions.task_classes || {};
  render(`
    <h2 class="section">The two invariants</h2>
    <div class="prose">
      <h3>Evidence</h3><p>${esc(m.the_evidence_invariant)}</p>
      <h3>Arithmetic</h3><p>${esc(m.the_arithmetic_invariant)}</p>
    </div>

    <h2 class="section">The formula</h2>
    <pre class="steps">${esc(m.formula)}</pre>
    <div class="derivation" style="margin-top:16px">
      <div class="measured"><h4>Measured</h4>
        <ul style="margin:0;padding-left:18px;font-size:13px">
          ${m.what_is_measured.map((x) => `<li>${esc(x)}</li>`).join('')}</ul></div>
      <div class="assumed"><h4>Assumed</h4>
        <ul style="margin:0;padding-left:18px;font-size:13px">
          ${m.what_is_assumed.map((x) => `<li>${esc(x)}</li>`).join('')}</ul></div>
    </div>
    <div class="banner" style="margin-top:16px"><strong>The largest uncertainty.</strong>
      ${esc(m.largest_uncertainty)}</div>

    <h2 class="section">Assumptions, per task class</h2>
    <p class="note">Straight from <code>config/estimation.yml</code>. Low / base / high for
    every value; the report's range is these bands recomputed end to end.</p>
    <table class="assump">
      <thead><tr><th>Task class</th><th class="num">handle</th><th class="num">per touch</th>
      <th class="num">rework</th><th class="num">waiting</th><th class="num">automatable</th></tr></thead>
      <tbody>${Object.entries(tc).map(([k, v]) => `<tr>
        <td>${esc(k.replace(/_/g, ' '))}</td>
        ${['handle_min', 'per_touch_min', 'rework_min', 'waiting_admin_min', 'automatable_share']
          .map((f) => `<td class="num">${esc(v[f].low)} / <strong>${esc(v[f].base)}</strong> / ${esc(v[f].high)}</td>`).join('')}
      </tr>`).join('')}</tbody>
    </table>

    <h2 class="section">What was read</h2>
    <table class="assump"><tbody>
      ${Object.entries({
        'files': m.corpus.files.toLocaleString(),
        'unique after dedup': m.corpus.unique_messages.toLocaleString(),
        'duplicates removed': `${m.corpus.duplicates_removed} in ${m.corpus.duplicate_groups} groups`,
        'task instances': m.corpus.task_instances.toLocaleString(),
        'shown to a model': m.corpus.messages_sent_to_a_model.toLocaleString(),
        'acknowledgements counted without a model': m.corpus.ack_only_messages.toLocaleString(),
        'distinct people': m.corpus.distinct_people.toLocaleString(),
        'date span': `${m.corpus.date_span.from} to ${m.corpus.date_span.to} (${m.corpus.date_span.months} months)`,
        'undated messages': m.corpus.undated_messages,
        'citations verified': s.evidence.citations_verified,
        'citations rejected': s.evidence.citations_quarantined,
        'citation tiers': JSON.stringify(s.evidence.tiers),
      }).map(([k, v]) => `<tr><td>${esc(k)}</td><td class="num">${esc(v)}</td></tr>`).join('')}
    </tbody></table>

    ${(m.corpus.generated_tables || []).map((g) => `
      <h2 class="section">A note on ${esc(g.path)}</h2>
      <div class="banner"><strong>This message is 5% of the corpus in one file, and its
      ${g.rows.toLocaleString()}-row table is machine-generated placeholder content, not
      business data. No quantity in this report is derived from it.</strong> The proof is
      arithmetic:</div>
      <pre class="steps">${g.proof.slice(1).map(esc).join('\n')}</pre>
      <p class="note">The prose above the table is genuine and is cited where relevant.</p>
    `).join('')}

    <h2 class="section">Check it yourself</h2>
    <ul class="note">${m.how_to_check_it_yourself.map((x) => `<li>${esc(x)}</li>`).join('')}</ul>
  `);
}

/* ---------------- drawer ---------------- */

function openDrawer(html) {
  $('#drawerBody').innerHTML = html;
  $('#drawer').hidden = false;
  $('#backdrop').hidden = false;
  $('#drawer').scrollTop = 0;
}
function closeDrawer() {
  $('#drawer').hidden = true;
  $('#backdrop').hidden = true;
}

boot();