import json
from gendiff.diff_finder import find_diff


def format_diff_stylish(diff_tree, indent="  "):
    lines = []
    lines.append("{")
    lines.extend(format_diff_items(diff_tree, indent))
    lines.append('}')
    return "\n".join(lines)


def format_diff_items(diff_tree, indent="  "):
    lines = []
    for item in diff_tree:
        node_type = item['type']
        key = item['key']
        value = item.get('value')

        if node_type == 'nested':
            nested_diff = format_nested_diff(item['children'], indent + '    ')
            lines.append(f"{indent}  {key}: {{")
            lines.extend(nested_diff)
            lines.append(f"{indent}  }}")

        elif node_type == 'added':
            formatted_value = format_value(value, indent + '  ')
            lines.append(f"{indent}+ {key}: {formatted_value}")

        elif node_type == 'removed':
            formatted_value = format_value(value, indent + '  ')
            lines.append(f"{indent}- {key}: {formatted_value}")

        elif node_type == 'changed':
            old_value = format_value(item['old_value'], indent + '  ')
            new_value = format_value(item['new_value'], indent + '  ')
            lines.append(f"{indent}- {key}: {old_value}")
            lines.append(f"{indent}+ {key}: {new_value}")

        elif node_type == 'unchanged':
            formatted_value = format_value(value, indent + '    ')
            lines.append(f"{indent}  {key}: {formatted_value}")

    return lines


def format_nested_diff(children, indent):
    lines = []
    lines.extend(format_diff_items(children, indent))
    return lines


def format_value(value, indent="  "):
    if isinstance(value, dict):
        lines = [f"{indent}    {k}: {format_value(v, indent + '    ')}"
                 for k, v in value.items()]
        return "{\n" + "\n".join(lines) + f"\n{indent}}}"
    else:
        return json.dumps(value, ensure_ascii=False).strip('"')


def generate_diff_stylish(data1, data2):
    diff_tree = find_diff(data1, data2)
    diff = format_diff_stylish(diff_tree)
    return diff
