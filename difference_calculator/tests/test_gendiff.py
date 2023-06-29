from difference_calculator.parser.parser import parser
import json
import yaml

PATH_TO_FILE1_JSON = 'difference_calculator/file1.json'
PATH_TO_FILE2_JSON = 'difference_calculator/file2.json'
PATH_TO_HEXLET_TEST_JSON = 'difference_calculator/tests/' \
                           'fixtures/hexlet_test.json'
PATH_TO_FAILURE_TEST_JSON = 'difference_calculator/tests/' \
                            'fixtures/fail_test.json'

PATH_TO_FILE1_YML = 'difference_calculator/file1.yml'
PATH_TO_FILE2_YML = 'difference_calculator/file2.yml'
PATH_TO_HEXLET_TEST_YML = 'difference_calculator/tests/' \
                          'fixtures/hexlet_test.yml'
PATH_TO_FAILURE_TEST_YML = 'difference_calculator/tests/' \
                           'fixtures/failure_test.yaml'


def test_hexlet_json():
    file = json.load(open(PATH_TO_HEXLET_TEST_JSON))
    file = json.dumps(file, indent=2)

    assert parser(PATH_TO_FILE1_JSON, PATH_TO_FILE2_JSON) == file


def test_failure_json():
    file = json.load(open(PATH_TO_FAILURE_TEST_JSON))
    file = json.dumps(file, indent=2)

    assert parser(PATH_TO_FILE1_JSON, PATH_TO_FILE2_JSON) != file


def test_hexlet_yml():
    with open(PATH_TO_HEXLET_TEST_YML) as f:
        fn = yaml.safe_load(f)
        file = json.dumps(fn, indent=2)

    assert parser(PATH_TO_FILE1_YML, PATH_TO_FILE2_YML) == file


def test_failure_yml():
    with open(PATH_TO_FAILURE_TEST_YML) as f:
        fn = yaml.safe_load(f)
        file = json.dumps(fn, indent=2)

    assert parser(PATH_TO_FILE1_YML, PATH_TO_FILE2_YML) != file
