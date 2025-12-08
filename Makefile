install:
	uv sync

check:
	uv run ruff check

fix:
	uv run ruff check --fix

run:
	uv run main.py