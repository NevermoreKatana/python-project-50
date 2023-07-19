from gendiff.parser import load_files
from gendiff.cli import cmd_gendiff
from gendiff.renderers.plain import gendiff_plain
from gendiff.renderers.json import gendiff_json
from gendiff.renderers.stylish import generate_diff_stylish



def generate_diff(PATH_TO_FILE1, PATH_TO_FILE2, style='stylish'):
    data1, data2 = load_files(PATH_TO_FILE1, PATH_TO_FILE2)
    if style == 'stylish':
        return generate_diff_stylish(data1, data2)
    elif style == 'plain':
        return gendiff_plain(data1, data2)
    elif style == 'json':
        return gendiff_json(data1, data2)


def gendiff():
    file1, file2, format = cmd_gendiff()
    diff = generate_diff(file1, file2, format)
    print(diff)
    return diff
