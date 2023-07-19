from gendiff.parser import load_files
from gendiff.cli import get_parser
from gendiff.renderers.plain import gendiff_plain
from gendiff.renderers.json import gendiff_json
from gendiff.renderers.stylish import generate_diff_stylish


def generate_diff(path_to_file1, path_to_file2, style='stylish'):
    data1, data2 = load_files(path_to_file1, path_to_file2)
    if style == 'stylish':
        return generate_diff_stylish(data1, data2)
    elif style == 'plain':
        return gendiff_plain(data1, data2)
    elif style == 'json':
        return gendiff_json(data1, data2)


def cmd_gendiff():
    parser = get_parser()
    args = parser.parse_args()
    if args.format is None:
        args.format = 'stylish'
    return args.first_file, args.second_file, args.format


def exec_app():
    file1, file2, format = cmd_gendiff()
    data1, data2 = load_files(file1, file2)
    diff = generate_diff(file1, file2, format)
    print(diff)
    return diff
