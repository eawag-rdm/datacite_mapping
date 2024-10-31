test:
	python -m pytest

test-all:
	# To use multiple pyenv versions you need to set all required local versions via:
    # pyenv local 3.8.16 3.9.16 3.10.11 3.11.3
	python -m tox

install:
	python -m pip install --upgrade .

install-dev:
	python -m pip install --upgrade -e .[dev]

.PHONY: docs
clean:
	rm -rdf __pycache__ .pytest_cache htmlcov .coverage build .ruff_cache .benchmarks tests/*/.benchmarks .tox
	make -C docs clean

style-check:
	ruff check --select I --fix
	ruff format
	ruff check

a-check:
	ruff check --watch

cov:
	pytest --cov-report term:skip-covered --cov-report html --cov=src tests

.PHONY: docs
docs:
	make -C docs html