PY=python3
COV=coverage
MAIN=src.main
TEST=src.test.run_tests
SOURCES=app/bot/

.PHONY: test

install:
	pip install --no-cache-dir -r requirements.txt

run:
	$(PY) -m $(MAIN)

test:
	$(PY) -m $(TEST)

coverage:
	$(COV) run -m --source=$(SOURCES) $(TEST)
	$(COV) report -m
	