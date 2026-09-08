.PHONY: run verify test serve doctor audit clean help
UV := uv run

help:
	@echo "make doctor   one real model call, fail fast with a remedy"
	@echo "make run      the full pipeline (one command; safe to re-run)"
	@echo "make verify   re-verify the published report; no model calls"
	@echo "make test     full test suite; no model calls"
	@echo "make serve    dashboard on http://localhost:8787"
	@echo "make audit    regenerate docs/AUDIT.md (25 random citations to hand-check)"

doctor:
	$(UV) python -m observe.cli doctor

run:
	$(UV) python -m observe.cli run

verify:
	$(UV) python -m observe.cli verify

test:
	$(UV) pytest -q

serve:
	$(UV) python -m observe.cli serve

audit:
	@mkdir -p docs
	@{ \
	  echo "# Audit sample"; echo; \
	  echo "25 citations chosen at random (seed 7) from the published report, with the"; \
	  echo "commands that reproduce each one from the raw corpus. This file is the literal"; \
	  echo "output of \`make audit\`; nothing here is hand-written."; echo; \
	  echo '```'; \
	  $(UV) python -m observe.cli verify --sample 25 --seed 7; \
	  echo '```'; \
	} > docs/AUDIT.md
	@echo "wrote docs/AUDIT.md"

clean:
	rm -rf out runs .observe-cache .pytest_cache .hypothesis
