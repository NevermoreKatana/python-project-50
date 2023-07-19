import json
from gendiff.parser import load_files
from gendiff.renderers.diff_finder import find_diff


def generate_diff(data1, data2):
    diff_tree = find_diff(data1, data2)
    diff = format_diff_stylish(diff_tree)
    return diff


def format_diff_stylish(diff_tree):
    lines = format_diff_items(diff_tree)
    return "{\n" + "\n".join(lines) + "\n}"


def format_diff_items(diff_tree, indent="  "):
    lines = []
    for item in diff_tree:
        node_type = item['type']
        key = item['key']

        if node_type == 'nested':
            nested_diff = format_diff_items(item['children'], indent + '    ')
            lines.append(f"{indent}  {key}: {{")
            lines.extend(nested_diff)
            lines.append(f"{indent}  }}")
        elif node_type in ('added', 'removed', 'unchanged'):
            value = format_value(item['value'], indent + '    ')
            sign = '+' if node_type == 'added' \
                else '-' if node_type == 'removed' else ' '
            lines.append(f"{indent}{sign} {key}: {value}")
        elif node_type == 'changed':
            old_value = format_value(item['old_value'], indent + '    ')
            new_value = format_value(item['new_value'], indent + '    ')
            lines.append(f"{indent}- {key}: {old_value}")
            lines.append(f"{indent}+ {key}: {new_value}")

    return lines


def format_value(value, indent):
    if isinstance(value, dict):
        lines = [f"{indent}    {k}: {format_value(v, indent + '    ')}"
                 for k, v in value.items()]
        return "{\n" + "\n".join(lines) + f"\n{indent}    }}"
    else:
        return json.dumps(value, ensure_ascii=False).strip('"')


def gendiff_stylish(data1, data2):
    diff = generate_diff(data1, data2)
    print(diff)
    return diff


def main():
    PATH_TO_FILE1_JSON = "example_files/file1.yml"
    PATH_TO_FILE2_JSON = "example_files/file2.yml"
    data1, data2 = load_files(PATH_TO_FILE1_JSON, PATH_TO_FILE2_JSON)
    gendiff_stylish(data1, data2)
