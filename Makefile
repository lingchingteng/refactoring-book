.PHONY: test
test:
	PYTHONPATH=. pytest tests

env:
	python -m venv venv
	python -m pip install -U -r requirements.txt