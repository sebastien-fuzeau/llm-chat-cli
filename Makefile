.PHONY: venv install run test fmt lint

venv:
	python -m venv .venv

install:
	. .venv/bin/activate && pip install -U pip && pip install -e ".[dev]"

run:
	. .venv/bin/activate && python -m src.main

test:
	. .venv/bin/activate && pytest -q

fmt:
	. .venv/bin/activate && ruff format .

lint:
	. .venv/bin/activate && ruff check .
