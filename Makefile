.PHONY: lint lint-full test clean

PY=python3
LINT=pycodestyle

# Warnings and errors to ignore 
# E501 - line too long
# W505 - doc line too long 
IGNORE=E501,W505

all: clean lint test

lint: 
	@echo "========== Linting =========="
	$(LINT) --ignore=$(IGNORE) --show-source *.py
	@echo "\n"

lint-full:
	@echo "========== Linting =========="
	$(LINT) --show-source --statistics *.py
	@echo "\n"

test: multivariate_hypergeometric.py test.py
	@echo "========== Testing =========="
	$(PY) test.py
	@echo "\n"

clean: 
	@echo "========== Cleaning ========="
	find . -name "*.pyc"7 -delete -print
	@echo "\n"
