import json
import yaml
from gendiff.parser import load_files

PATH_TO_FILE1_JSON = 'tests/fixtures/file1.json'
PATH_TO_FILE2_JSON = 'tests/fixtures/file2.json'

PATH_TO_FILE1_YML = 'tests/fixtures/file1.yml'

PATH_TO_TEST_FILE_YML = 'tests/fixtures/test_yml.yml'


def test_parser_json():
    with open(PATH_TO_FILE1_JSON, 'r') as file1:
        with open(PATH_TO_FILE2_JSON, 'r') as file2:
            expected_data1 = json.load(file1)
            expected_data2 = json.load(file2)

    data1, data2 = load_files(PATH_TO_FILE1_JSON, PATH_TO_FILE2_JSON)

    assert expected_data1 == data1

    assert expected_data2 == data2


def test_parser_yml():
    with open(PATH_TO_FILE1_YML, 'r') as file1:
        with open(PATH_TO_TEST_FILE_YML, 'r') as file2:
            expected_data1 = yaml.safe_load(file1)
            expected_data2 = yaml.safe_load(file2)

    data1, data2 = load_files(PATH_TO_FILE1_YML, PATH_TO_TEST_FILE_YML)

    assert expected_data1 == data1

    assert expected_data2 == data2
