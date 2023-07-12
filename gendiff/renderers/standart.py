import json
from gendiff.parser import file_type

def generate_diff(data1, data2):
    def build_diff(node1, node2, indent):
        diff = []
        keys = sorted(set(list(node1.keys()) + list(node2.keys())))

        for key in keys:
            value1 = node1.get(key)
            value2 = node2.get(key)

            if key not in node2:
                diff.append(f"{indent}- {key}: {format_value(value1, indent)}")
            elif key not in node1:
                diff.append(f"{indent}+ {key}: {format_value(value2, indent)}")
            elif isinstance(value1, dict) and isinstance(value2, dict):
                diff.append(f"{indent}  {key}:")
                diff.extend(build_diff(value1, value2, indent + "    "))
            elif value1 == value2:
                diff.append(f"{indent}  {key}: {format_value(value1, indent)}")
            else:
                diff.append(f"{indent}- {key}: {format_value(value1, indent)}")
                diff.append(f"{indent}+ {key}: {format_value(value2, indent)}")

        return diff

    def format_value(value, indent):
        if isinstance(value, dict):
            lines = [f"{indent}    {k}: {format_value(v, indent + '  ')}" for k, v in value.items()]
            return "{\n" + "\n".join(lines) + f"\n{indent}  }}"
        else:
            return json.dumps(value).lower()

    diff = build_diff(data1, data2, "")

    return "{\n" + "\n".join(diff) + "\n}"
def main():
    PATH_TO_FILE1_JSON = "example_files/file1.json"
    PATH_TO_FILE2_JSON = "example_files/file2.json"
    data1, data2 = file_type(PATH_TO_FILE1_JSON, PATH_TO_FILE2_JSON)
    diff = generate_diff(data1, data2)
    print(diff)
