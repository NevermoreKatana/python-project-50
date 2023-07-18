import json
from gendiff.parser import load_files
from gendiff.renderers.diff_finder import find_diff
from gendiff.renderers.json import (
    compare_values,
    generate_diff_json,
    format_diff_json,
    generate_diff_dict_json,
    gendiff_json
)



def test_format_diff_json():
    # Тестирование форматирования разницы в словарь
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

    # Тестирование форматирования пустой разницы
    diff_tree = []
    expected = {}
    assert format_diff_json(diff_tree) == expected


