.PHONY: install sync test lint format typecheck check clean build

install:
	uv sync

sync:
	uv sync

test:
	uv run pytest

lint:
	uv run ruff check .

format:
	uv run ruff format .

typecheck:
	uv run mypy src

check:
	uv run ruff check .
	uv run mypy src
	uv run pytest

build:
	uv build

clean:
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .ruff_cache
	rm -rf dist
	rm -rf build
	find . -type d -name "__pycache__" -exec rm -rf {} +
