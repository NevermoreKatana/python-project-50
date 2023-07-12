import json
from gendiff.parser import load_files


def generate_diff_plain(data1, data2, path=""):
    diff = build_diff(data1, data2, path)
    return "\n".join(diff)


def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return json.dumps(value)


def build_diff(node1, node2, path):
    diff = []

    keys = sorted(set(list(node1.keys()) + list(node2.keys())))

    for key in keys:
        value1 = node1.get(key)
        value2 = node2.get(key)

        if key not in node2:
            diff.append(f"Property '{path}{key}' was removed")
        elif key not in node1:
            diff.append(f"Property '{path}{key}' "
                        f"was added with value: {format_value(value2)}")
        elif isinstance(value1, dict) and isinstance(value2, dict):
            diff.extend(build_diff(value1, value2, f"{path}{key}."))
        elif value1 == value2:
            continue
        else:
            diff.append(f"Property '{path}{key}' was updated.From "
                        f"{format_value(value1)} to {format_value(value2)}")

    return diff


def main():
    PATH_TO_FILE1_JSON = "example_files/file1.json"
    PATH_TO_FILE2_JSON = "example_files/file2.json"
    data1, data2 = load_files(PATH_TO_FILE1_JSON, PATH_TO_FILE2_JSON)
    diff = generate_diff_plain(data1, data2)
    print(diff)
