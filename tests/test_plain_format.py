from gendiff.renderers.plain import generate_diff_plain
from gendiff.parser import file_type


PATH_TO_FILE1_JSON = 'example_files/file1.json'
PATH_TO_FILE2_JSON = 'example_files/file2.json'

PATH_TO_FILE1_YML = 'example_files/file1.yml'
PATH_TO_FILE2_YML = 'example_files/file2.yml'

PATH_TO_HEXLET_TEST = 'tests/fixtures/plain_test.txt'
PATH_TO_FAILURE_TEST = 'tests/fixtures/plain_failure_test.txt'


def test_plain_json():
    with open(PATH_TO_HEXLET_TEST, 'r') as file:
        file = file.read()

    data1, data2 = file_type(PATH_TO_FILE1_JSON, PATH_TO_FILE2_JSON)
    result = generate_diff_plain(data1, data2)

    assert result == file


def test_plain_yml():
    with open(PATH_TO_HEXLET_TEST, 'r') as file:
        file = file.read()

    data1, data2 = file_type(PATH_TO_FILE1_YML, PATH_TO_FILE2_YML)
    result = generate_diff_plain(data1, data2)

    assert result == file


def test_failure_plain_json():
    with open(PATH_TO_FAILURE_TEST, 'r') as file:
        file = file.read()

    data1, data2 = file_type(PATH_TO_FILE1_JSON, PATH_TO_FILE2_JSON)
    result = generate_diff_plain(data1, data2)

    assert result != file


def test_failure_plain_yml():
    with open(PATH_TO_FAILURE_TEST, 'r') as file:
        file = file.read()

    data1, data2 = file_type(PATH_TO_FILE1_YML, PATH_TO_FILE2_YML)
    result = generate_diff_plain(data1, data2)

    assert result != file



