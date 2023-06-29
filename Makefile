install:
	poetry install
build:
	 poetry build

cmd_gendiff:
	poetry run cmd_gendiff -h
gendiff:
	poetry run gendiff
test:
	poetry run pytest
test-coverage:
	poetry run pytest --cov=difference_calculator --cov-report xml
pars:
	poetry run parser
publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

make lint:
	poetry run flake8 difference_calculator