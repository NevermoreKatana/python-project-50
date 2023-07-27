import json
from gendiff.renderers.json import generate_diff_json
from gendiff.parser import load_files

PATH_TO_FILE1_JSON = 'tests/fixtures/file1.json'
PATH_TO_FILE2_JSON = 'tests/fixtures/file2.json'

PATH_TO_FILE1_YML = 'tests/fixtures/file1.yml'
PATH_TO_FILE2_YML = 'tests/fixtures/file2.yml'

PATH_TO_TEST_FILE_JSON = 'tests/fixtures/test_json.json'
PATH_TO_TEST_FAILURE_FILE_JSON = 'tests/fixtures/test_failure_json.json'

PATH_TO_TEST_FILE_YML = 'tests/fixtures/test_yml.yml'
PATH_TO_TEST_FAILURE_FILE_YML = 'tests/fixtures/test_failure_yaml.yaml'


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
