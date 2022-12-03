.PHONY: setup-env
setup-env:
	poetry env use python3.11
	poetry install --without dev

.PHONY: setup-env-dev
setup-env-dev:
	poetry install --with dev

.PHONY: run
run: setup-env
	poetry run python src/main.py

.PHONY: submit_part_a
submit_part_a: setup-env
	poetry run python src/submit.py a

.PHONY: submit_part_b
submit_part_b: setup-env
	poetry run python src/submit.py b

.PHONY: format
format: setup-env-dev
	poetry run black .

.PHONY: lint
lint: setup-env-dev
	poetry run flake8 .
	poetry run mypy .
	poetry run black --check .