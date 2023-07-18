

def find_diff(node1, node2):
    diff_tree = build_diff_tree(node1, node2)
    return diff_tree


def build_diff_tree(node1, node2):
    diff_tree = []
    keys = sorted(set(list(node1.keys()) + list(node2.keys())))

    for key in keys:
        value1 = node1.get(key)
        value2 = node2.get(key)

        if key not in node2:
            diff_tree.append({
                'type': 'removed',
                'key': key,
                'value': value1
            })
        elif key not in node1:
            diff_tree.append({
                'type': 'added',
                'key': key,
                'value': value2
            })
        elif isinstance(value1, dict) and isinstance(value2, dict):
            nested_diff = build_diff_tree(value1, value2)
            diff_tree.append({
                'type': 'nested',
                'key': key,
                'children': nested_diff
            })
        elif value1 == value2:
            diff_tree.append({
                'type': 'unchanged',
                'key': key,
                'value': value1
            })
        else:
            diff_tree.append({
                'type': 'changed',
                'key': key,
                'old_value': value1,
                'new_value': value2
            })

    return diff_tree
