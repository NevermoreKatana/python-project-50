from difference_calculator.formatting.plain_format import generate_diff_plain
from difference_calculator.parser.parser import pars
import json
import yaml

PATH_TO_FILE1_JSON = 'difference_calculator/file1.json'
PATH_TO_FILE2_JSON = 'difference_calculator/file2.json'

PATH_TO_FILE1_YML = 'difference_calculator/file1.yml'
PATH_TO_FILE2_YML = 'difference_calculator/file2.yml'

PATH_TO_HEXLET_TEST = 'difference_calculator/tests/' \
                           'fixtures/plain_test.txt'
PATH_TO_FAILURE_TEST = 'difference_calculator/tests/' \
                            'fixtures/plain_failure_test.txt'




def test_plain_json():
    with open(PATH_TO_HEXLET_TEST, 'r') as file:
        file = file.read()

    data1, data2 = pars(PATH_TO_FILE1_JSON, PATH_TO_FILE2_JSON)
    result = generate_diff_plain(data1, data2)

    assert result == file


def test_plain_yml():
    with open(PATH_TO_HEXLET_TEST, 'r') as file:
        file = file.read()

    data1, data2 = pars(PATH_TO_FILE1_YML, PATH_TO_FILE2_YML)
    result = generate_diff_plain(data1, data2)

    assert result == file


def test_failure_plain_json():
    with open(PATH_TO_FAILURE_TEST, 'r') as file:
        file = file.read()

    data1, data2 = pars(PATH_TO_FILE1_JSON, PATH_TO_FILE2_JSON)
    result = generate_diff_plain(data1, data2)

    assert result != file


def test_failure_plain_yml():
    with open(PATH_TO_FAILURE_TEST, 'r') as file:
        file = file.read()

    data1, data2 = pars(PATH_TO_FILE1_YML, PATH_TO_FILE2_YML)
    result = generate_diff_plain(data1, data2)

    assert result != file