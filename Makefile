.PHONY: install
install:
	python3 -m venv venv && source venv/bin/activate && python -m pip install . && python -m pip install ".[test,lint]"

.PHONY: lint
lint:
	flake8 src

.PHONY: test
test:
	tox
