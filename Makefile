install:
	poetry install
build:
	 poetry build

test:
	poetry run gendiff -h


publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

make lint:
	poetry run flake8 difference_calculator