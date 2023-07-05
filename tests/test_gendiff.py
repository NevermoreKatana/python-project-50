import json
import yaml
from difference_calculator.parser import file_type
from difference_calculator.renderers.standart import (
    compare_values,
    format_diff,
    generate_diff_dict,
)


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

    data1, data2 = file_type(PATH_TO_FILE1_JSON, PATH_TO_FILE2_JSON)
    result = generate_diff_dict(data1, data2)

    assert result == file


def test_failure_json():
    file = json.load(open(PATH_TO_FAILURE_TEST_JSON))
    file = json.dumps(file, indent=2)

    data1, data2 = file_type(PATH_TO_FILE1_JSON, PATH_TO_FILE2_JSON)
    result = generate_diff_dict(data1, data2)

    assert result != file


def test_hexlet_yml():
    with open(PATH_TO_HEXLET_TEST_YML) as f:
        fn = yaml.safe_load(f)
        file = json.dumps(fn, indent=2)

    data1, data2 = file_type(PATH_TO_FILE1_YML, PATH_TO_FILE2_YML)
    result = generate_diff_dict(data1, data2)

    assert result == file


def test_failure_yml():
    with open(PATH_TO_FAILURE_TEST_YML) as f:
        fn = yaml.safe_load(f)
        file = json.dumps(fn, indent=2)

    data1, data2 = file_type(PATH_TO_FILE1_YML, PATH_TO_FILE2_YML)
    result = generate_diff_dict(data1, data2)

    assert result != file


def test_compare_values_same_values():
    value1 = 10
    value2 = 10
    result = compare_values(value1, value2)
    assert result == {'status': 'unchanged', 'value': 10}

def test_compare_values_different_values():
    value1 = 10
    value2 = 20
    result = compare_values(value1, value2)
    assert result == {'status': 'changed', 'old_value': 10, 'new_value': 20}

def test_format_diff():
    diff = {
        'key1': {'status': 'removed', 'value': 'value1'},
        'key2': {'status': 'changed', 'old_value': 'value2', 'new_value': 'new_value'},
        'key3': {'status': 'added', 'value': 'value3'}
    }
    result = format_diff(diff)
    expected_result = {
        '- key1': 'value1',
        '- key2': 'value2',
        '+ key2': 'new_value',
        '+ key3': 'value3'
    }
    assert result == expected_result

def test_generate_diff_dict():
    data1 = {'key1': 'value1', 'key2': 'value2'}
    data2 = {'key2': 'new_value', 'key3': 'value3'}
    result = generate_diff_dict(data1, data2)
    expected_result = """{
  "- key1": "value1",
  "- key2": "value2",
  "+ key2": "new_value",
  "+ key3": "value3"
}"""
    assert result.strip() == expected_result.strip()
