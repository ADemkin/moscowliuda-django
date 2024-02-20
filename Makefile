PROJECT := moscowliuda
POETRY := poetry
RUN := ${POETRY} run

.PHONY: install update lint-mypy lint-black lint-ruff lint fmt-black fmt

help:
	@echo "install - install dependencies"
	@echo "update - update dependencies"
	@echo "lint - run all linters"
	@echo "fmt - run all formatters"



install:
	$(POETRY) install
	$(MAKE) populate-db

update:
	$(POETRY) update

lint-mypy:
	$(RUN) mypy --install-types $(PROJECT)

lint-black:
	$(RUN) black --check $(PROJECT)

lint-ruff:
	$(RUN) ruff check $(PROJECT)

lint: lint-black lint-ruff
	@echo "Linting done."

fmt-black:
	$(RUN) black $(PROJECT)

fmt: fmt-black
	@echo "Formatting done."

populate-db:
	$(RUN)	python	add_item_to_db.py
