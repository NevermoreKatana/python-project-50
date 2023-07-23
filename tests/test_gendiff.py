from gendiff.diff_finder import find_diff


def test_find_diff_changed_value():
    node1 = {'a': 1, 'b': 2}
    node2 = {'a': 1, 'b': 3}
    expected_diff = [{'key': 'a', 'type': 'unchanged', 'value': 1},
                     {'key': 'b', 'new_value': 3, 'old_value': 2,
                      'type': 'changed'}]
    assert find_diff(node1, node2) == expected_diff


def test_find_diff_same_nodes():
    node1 = {'a': 1, 'b': 2, 'c': 3}
    node2 = {'a': 1, 'b': 2, 'c': 3}
    expected_diff = [{'key': 'a', 'type': 'unchanged', 'value': 1},
                     {'key': 'b', 'type': 'unchanged', 'value': 2},
                     {'key': 'c', 'type': 'unchanged', 'value': 3}]
    assert find_diff(node1, node2) == expected_diff


def test_find_diff_removed_key():
    node1 = {'a': 1, 'b': 2, 'c': 3}
    node2 = {'a': 1, 'b': 2}
    expected_diff = [{'key': 'a', 'type': 'unchanged', 'value': 1},
                     {'key': 'b', 'type': 'unchanged', 'value': 2},
                     {'key': 'c', 'type': 'removed', 'value': 3}]
    assert find_diff(node1, node2) == expected_diff
