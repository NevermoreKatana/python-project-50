from gendiff.parser import cmd_gendiff
from gendiff.parser import load_files
from gendiff.renderers.plain import gendiff_plain
from gendiff.renderers.json import gendiff_json
from gendiff.renderers.stylish import generate_diff_stylish



def main():
    PATH_TO_FILE1, PATH_TO_FILE2, FORMAT = cmd_gendiff()
    data1, data2 = load_files(PATH_TO_FILE1, PATH_TO_FILE2)
    if FORMAT == 'plain':
        gendiff_plain(data1, data2)
    elif FORMAT == 'json':
        gendiff_json(data1, data2)
    else:
        d = generate_diff_stylish(data1, data2)
        print(d)


def generate_diff(PATH_TO_FILE1, PATH_TO_FILE2, style='stylish'):
    data1, data2 = load_files(PATH_TO_FILE1, PATH_TO_FILE2)
    if style == 'stylish':
        diff = generate_diff_stylish(data1, data2)
    elif style == 'plain':
        diff = gendiff_plain(data1, data2)
    elif style == 'json':
        diff = gendiff_json(data1, data2)
    return diff
