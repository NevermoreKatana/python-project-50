from gendiff.renderers.json import (
    format_diff_json,
)


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
