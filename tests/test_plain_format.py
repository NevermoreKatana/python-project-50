import json
from gendiff.parser import load_files

from gendiff.renderers.plain import (
    generate_diff_plain,
    format_diff_plain,
    format_value,
    gendiff_plain
)

PATH_TO_FILE1_YML = "example_files/file1.yml"
PATH_TO_FILE2_YML = "example_files/file2.yml"

PATH_TO_FILE1_JSON = "example_files/file1.json"
PATH_TO_FILE2_JSON = "example_files/file2.json"

RESULT_FILE = 'tests/fixtures/plain_test.txt'
FAILURE_FILE = 'tests/fixtures/plain_failure_test.txt'

def test_generate_diff_plain():
    # Тестирование генерации разницы между двумя словарями в формате plain
    data1 = {'a': 1, 'b': 2}
    data2 = {'a': 1, 'b': 3}
    expected = "Property 'b' was updated. From 2 to 3"
    assert generate_diff_plain(data1, data2) == expected

    # Тестирование генерации разницы между двумя пустыми словарями в формате plain
    data1 = {}
    data2 = {}
    expected = ""
    assert generate_diff_plain(data1, data2) == expected

def test_format_diff_plain():
    # Тестирование форматирования разницы в формате plain
    diff_tree = [
        {'type': 'added', 'key': 'a', 'value': 1},
        {'type': 'removed', 'key': 'b', 'value': 2},
        {'type': 'changed', 'key': 'c', 'old_value': 3, 'new_value': 4},
        {'type': 'nested', 'key': 'd', 'children': [
            {'type': 'added', 'key': 'e', 'value': 5}
        ]}
    ]
    expected = "Property 'a' was added with value: 1\n"\
               "Property 'b' was removed\n"\
               "Property 'c' was updated. From 3 to 4\n"\
               "Property 'd.e' was added with value: 5"
    assert format_diff_plain(diff_tree) == expected

    # Тестирование форматирования пустой разницы в формате plain
    diff_tree = []
    expected = ""
    assert format_diff_plain(diff_tree) == expected

def test_format_value():
    # Тестирование форматирования значения
    value = {'a': 1, 'b': 2}
    expected = "[complex value]"
    assert format_value(value) == expected

    value = "test"
    expected = "'test'"
    assert format_value(value) == expected

    value = 10
    expected = json.dumps(10)
    assert format_value(value) == expected

def test_gendiff_plain_json():
    data1, data2 = load_files(PATH_TO_FILE1_JSON, PATH_TO_FILE2_JSON)
    with open(RESULT_FILE, 'r') as f:
        expected = f.read()

    assert gendiff_plain(data1, data2) == expected

def test_gendiff_plain_json_failure():
    data1, data2 = load_files(PATH_TO_FILE1_JSON, PATH_TO_FILE2_JSON)
    with open(FAILURE_FILE, 'r') as f:
        expected = f.read()

    assert gendiff_plain(data1, data2) != expected

def test_gendiff_plain_yml():
    data1, data2 = load_files(PATH_TO_FILE1_YML, PATH_TO_FILE2_YML)
    with open(RESULT_FILE, 'r') as f:
        expected = f.read()

    assert gendiff_plain(data1, data2) == expected

def test_gendiff_plain_yml_failure():
    data1, data2 = load_files(PATH_TO_FILE1_YML, PATH_TO_FILE2_YML)
    with open(FAILURE_FILE, 'r') as f:
        expected = f.read()

    assert gendiff_plain(data1, data2) != expected