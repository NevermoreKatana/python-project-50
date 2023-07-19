install:
	poetry install

build:
	 poetry build

test:
	poetry run pytest -vv

t:
	poetry run t
cmd:
	poetry run cmd -h
g:
	poetry run gendiff example_files/file1.json example_files/file2.json

entry:
	 poetry run entry example_files/file1.json example_files/file2.json

entry_p:
	 poetry run entry -f plain

entry_j:
	 poetry run entry -f json example_files/file1.json example_files/file2.json

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

pars:
	poetry run parser

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

make lint:
	poetry run flake8