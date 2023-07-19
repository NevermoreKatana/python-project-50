import json
from gendiff.renderers.json import format_diff_json, generate_diff_json
from gendiff.parser import load_files

PATH_TO_FILE1_JSON = 'example_files/file1.json'
PATH_TO_FILE2_JSON = 'example_files/file2.json'

PATH_TO_FILE1_YML = 'example_files/file1.yml'
PATH_TO_FILE2_YML = 'example_files/file2.yml'

PATH_TO_TEST_FILE_JSON = 'tests/fixtures/test_json.json'
PATH_TO_TEST_FAILURE_FILE_JSON = 'tests/fixtures/test_failure_json.json'

PATH_TO_TEST_FILE_YML = 'tests/fixtures/test_yml.yml'
PATH_TO_TEST_FAILURE_FILE_YML = 'tests/fixtures/test_failure_yaml.yaml'


def test_format_diff_json():
    diff_tree = [
        {'type': 'added', 'key': 'a', 'value': 1},
        {'type': 'removed', 'key': 'b', 'value': 2},
        {'type': 'changed', 'key': 'c', 'new_value': 3},
        {'type': 'unchanged', 'key': 'd', 'value': 4}
    ]
    expected = {
        'a': 1,
        'b': 2,
        'c': 3,
        'd': 4
    }
    assert format_diff_json(diff_tree) == expected

    diff_tree = []
    expected = {}
    assert format_diff_json(diff_tree) == expected


def test_json_format_json():
    with open(PATH_TO_TEST_FILE_JSON, 'r') as file:
        expected = json.load(file)
    data1, data2 = load_files(PATH_TO_FILE1_JSON, PATH_TO_FILE2_JSON)

    assert generate_diff_json(data1, data2) == expected


def test_json_format_yml():
    with open(PATH_TO_TEST_FILE_YML, 'r') as file:
        expected = json.load(file)

    data1, data2 = load_files(PATH_TO_FILE1_JSON, PATH_TO_FILE2_JSON)

    assert generate_diff_json(data1, data2) == expected


def test__failure_json_format_json():
    with open(PATH_TO_TEST_FAILURE_FILE_JSON, 'r') as file:
        expected = json.load(file)
    data1, data2 = load_files(PATH_TO_FILE1_JSON, PATH_TO_FILE2_JSON)

    assert generate_diff_json(data1, data2) != expected


def test_failure_json_format_yml():
    with open(PATH_TO_TEST_FAILURE_FILE_YML, 'r') as file:
        expected = json.load(file)

    data1, data2 = load_files(PATH_TO_FILE1_JSON, PATH_TO_FILE2_JSON)

    assert generate_diff_json(data1, data2) != expected
