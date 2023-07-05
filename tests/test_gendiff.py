from difference_calculator.parser.parser import pars
from difference_calculator.gendiff.generate_diff import generate_diff_dict
import json
import yaml

PATH_TO_FILE1_JSON = 'example_files/file1.json'
PATH_TO_FILE2_JSON = 'example_files/file2.json'
PATH_TO_HEXLET_TEST_JSON = 'tests/fixtures/hexlet_test.json'
PATH_TO_FAILURE_TEST_JSON = 'tests/fixtures/fail_test.json'

PATH_TO_FILE1_YML = 'example_files/file1.yml'
PATH_TO_FILE2_YML = 'example_files/file2.yml'

PATH_TO_HEXLET_TEST_YML = 'tests/fixtures/hexlet_test.yml'
PATH_TO_FAILURE_TEST_YML = 'tests/fixtures/failure_test.yaml'


def test_hexlet_json():
    file = json.load(open(PATH_TO_HEXLET_TEST_JSON))
    file = json.dumps(file, indent=2)

    data1, data2 = pars(PATH_TO_FILE1_JSON, PATH_TO_FILE2_JSON)
    result = generate_diff_dict(data1, data2)

    assert result == file


def test_failure_json():
    file = json.load(open(PATH_TO_FAILURE_TEST_JSON))
    file = json.dumps(file, indent=2)

    data1, data2 = pars(PATH_TO_FILE1_JSON, PATH_TO_FILE2_JSON)
    result = generate_diff_dict(data1, data2)

    assert result != file


def test_hexlet_yml():
    with open(PATH_TO_HEXLET_TEST_YML) as f:
        fn = yaml.safe_load(f)
        file = json.dumps(fn, indent=2)

    data1, data2 = pars(PATH_TO_FILE1_YML, PATH_TO_FILE2_YML)
    result = generate_diff_dict(data1, data2)

    assert result == file


def test_failure_yml():
    with open(PATH_TO_FAILURE_TEST_YML) as f:
        fn = yaml.safe_load(f)
        file = json.dumps(fn, indent=2)

    data1, data2 = pars(PATH_TO_FILE1_YML, PATH_TO_FILE2_YML)
    result = generate_diff_dict(data1, data2)

    assert result != file
