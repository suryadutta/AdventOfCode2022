.PHONY: run
run:
	poetry run python main.py

.PHONY: format
format:
	poetry run black .

.PHONY: lint
lint:
	poetry run flake8 .
	poetry run mypy .
	poetry run black --check .