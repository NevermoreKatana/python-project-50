install:
	poetry install

build:
	 poetry build

test:
	poetry run pytest -vv

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

make lint:
	poetry run flake8