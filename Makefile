.PHONY: lint test clean

PY=python3
LINT=pycodestyle


all: clean lint test

lint: 
	$(LINT) --show-source *.py

test: test.py multivariate_hypergeometric.py
	$(PY) test.py

clean: 
	find . -name "*.pyc" -delete -print
