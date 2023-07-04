import json

from difference_calculator.formatting.json_format import generate_diff_dict_json
from difference_calculator.parser.parser import pars


PATH_TO_FILE1_JSON = 'difference_calculator/file1.json'
PATH_TO_FILE2_JSON = 'difference_calculator/file2.json'

PATH_TO_FILE1_YML = 'difference_calculator/file1.yml'
PATH_TO_FILE2_YML = 'difference_calculator/file2.yml'

PATH_TO_HEXLET_TEST = 'difference_calculator/tests/' \
                           'fixtures/test_json_format.json'
PATH_TO_FAILURE_TEST = 'difference_calculator/tests/' \
                            'fixtures/fail_test_json_format.json'


def test_jsonFormat_json():
    file = json.load(open(PATH_TO_HEXLET_TEST))
    file = json.dumps(file, indent=2)

    data1, data2 = pars(PATH_TO_FILE1_JSON, PATH_TO_FILE2_JSON)
    result = generate_diff_dict_json(data1, data2)

    assert result == file


def test_plain_yml():
    file = json.load(open(PATH_TO_HEXLET_TEST))
    file = json.dumps(file, indent=2)

    data1, data2 = pars(PATH_TO_FILE1_YML, PATH_TO_FILE2_YML)
    result = generate_diff_dict_json(data1, data2)

    assert result == file


def test_failure_plain_json():
    file = json.load(open(PATH_TO_FAILURE_TEST))
    file = json.dumps(file, indent=2)

    data1, data2 = pars(PATH_TO_FILE1_JSON, PATH_TO_FILE2_JSON)
    result = generate_diff_dict_json(data1, data2)

    assert result != file


def test_failure_plain_yml():
    file = json.load(open(PATH_TO_FAILURE_TEST))
    file = json.dumps(file, indent=2)

    data1, data2 = pars(PATH_TO_FILE1_YML, PATH_TO_FILE2_YML)
    result = generate_diff_dict_json(data1, data2)

    assert result != file
