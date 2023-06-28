from difference_calculator.gendiff.generate_diff import generate_diff
import json

PATH_TO_FILE1 = 'difference_calculator/file1.json'
PATH_TO_FILE2 = 'difference_calculator/file2.json'
PATH_TO_HEXLET_TEST = 'difference_calculator/tests/fixtures/hexlet_test.json'
PATH_TO_FAILURE_TEST = 'difference_calculator/tests/fixtures/fail_test.json'


def test_hexlet():
    file = json.load(open(PATH_TO_HEXLET_TEST))
    file = json.dumps(file, indent=2)
    assert generate_diff(PATH_TO_FILE1, PATH_TO_FILE2) == file


def test_failure():
    file = json.load(open(PATH_TO_FAILURE_TEST))
    file = json.dumps(file, indent=2)
    assert generate_diff(PATH_TO_FILE1, PATH_TO_FILE2) != file
