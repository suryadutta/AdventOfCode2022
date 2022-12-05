PHONY: check-day
check-day:
ifndef AOC_DAY
	$(error AOC_DAY must be set)
endif

.PHONY: setup-env
setup-env:
	poetry env use python3.11
	poetry install --without dev

.PHONY: setup-env-dev
setup-env-dev:
	poetry env use python3.11
	poetry install --with dev

.PHONY: run
run: setup-env check-day
	PYTHONPATH="$${PWD}" poetry run python src/run.py

.PHONY: submit_part_a
submit_part_a: setup-env check-day
	PYTHONPATH="$${PWD}" poetry run python src/submit.py a

.PHONY: submit_part_b
submit_part_b: setup-env set-year check-day
	PYTHONPATH="$${PWD}" poetry run python src/submit.py b

.PHONY: test
test: setup-env-dev
	PYTHONPATH="$${PWD}" poetry run python -m pytest \
		--cov $${PWD}/src \
		-v tests/

.PHONY: format
format: setup-env-dev
	poetry run black .

.PHONY: lint
lint: setup-env-dev
	poetry run flake8 .
	poetry run mypy .
	poetry run black --check .