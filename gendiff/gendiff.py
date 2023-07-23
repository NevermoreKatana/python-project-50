from gendiff.parser import load_files
from gendiff.cli import get_parser
from gendiff.renderers.plain import generate_diff_plain
from gendiff.renderers.json import generate_diff_json
from gendiff.renderers.stylish import generate_diff_stylish


def generate_diff(path_to_file1, path_to_file2, style='stylish'):
    data1, data2 = load_files(path_to_file1, path_to_file2)
    if style == 'stylish':
        return generate_diff_stylish(data1, data2)
    elif style == 'plain':
        return generate_diff_plain(data1, data2)
    elif style == 'json':
        return generate_diff_json(data1, data2)


def get_argument_generation_references():
    parser = get_parser()
    args = parser.parse_args()
    if args.format is None:
        args.format = 'stylish'
    return args.first_file, args.second_file, args.format
