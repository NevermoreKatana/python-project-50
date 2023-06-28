install:
	poetry install
build:
	 poetry build

cmd_gendiff:
	poetry run cmd_gendiff -h
gendiff:
	poetry run test
test:
	poetry run pytest
publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

make lint:
	poetry run flake8 difference_calculator