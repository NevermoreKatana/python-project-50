import json

from difference_calculator.renderers.json import generate_diff_dict_json
from difference_calculator.parser import file_type


PATH_TO_FILE1_JSON = 'example_files/file1.json'
PATH_TO_FILE2_JSON = 'example_files/file2.json'

PATH_TO_FILE1_YML = 'example_files/file1.yml'
PATH_TO_FILE2_YML = 'example_files/file2.yml'

PATH_TO_HEXLET_TEST = 'tests/fixtures/test_json_format.json'
PATH_TO_FAILURE_TEST = 'tests/fixtures/fail_test_json_format.json'


def test_jsonFormat_json():
    file = json.load(open(PATH_TO_HEXLET_TEST))
    file = json.dumps(file, indent=2)

    data1, data2 = file_type(PATH_TO_FILE1_JSON, PATH_TO_FILE2_JSON)
    result = generate_diff_dict_json(data1, data2)

    assert result == file


def test_plain_yml():
    file = json.load(open(PATH_TO_HEXLET_TEST))
    file = json.dumps(file, indent=2)

    data1, data2 = file_type(PATH_TO_FILE1_YML, PATH_TO_FILE2_YML)
    result = generate_diff_dict_json(data1, data2)

    assert result == file


def test_failure_plain_json():
    file = json.load(open(PATH_TO_FAILURE_TEST))
    file = json.dumps(file, indent=2)

    data1, data2 = file_type(PATH_TO_FILE1_JSON, PATH_TO_FILE2_JSON)
    result = generate_diff_dict_json(data1, data2)

    assert result != file


def test_failure_plain_yml():
    file = json.load(open(PATH_TO_FAILURE_TEST))
    file = json.dumps(file, indent=2)

    data1, data2 = file_type(PATH_TO_FILE1_YML, PATH_TO_FILE2_YML)
    result = generate_diff_dict_json(data1, data2)

    assert result != file
