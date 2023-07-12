install:
	poetry install

build:
	 poetry build

cmd_gendiff:
	poetry run cmd_gendiff -h

test:
	poetry run pytest

t:
	poetry run t

entry:
	 poetry run entry example_files/file1.json example_files/file2.json

entry_p:
	 poetry run entry -f plain example_files/file1.json example_files/file2.json

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
	poetry run flake8 gendiff