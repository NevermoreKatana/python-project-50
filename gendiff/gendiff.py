from gendiff.renderers.stylish import generate_diff_stylish
from gendiff.parser import load_files
from gendiff.renderers.plain import generate_diff_plain
from gendiff.parser import cmd_gendiff
from gendiff.renderers.json import generate_diff_dict_json


def main():
    PATH_TO_FILE1, PATH_TO_FILE2, FORMAT = cmd_gendiff()
    data1, data2 = load_files(PATH_TO_FILE1, PATH_TO_FILE2)
    if FORMAT == 'plain':
        generate_diff_plain(data1, data2)
    elif FORMAT == 'json':
        generate_diff_dict_json(data1, data2)
    else:
        d = generate_diff_stylish(data1, data2)
        print(d)


def generate_diff(PATH_TO_FILE1, PATH_TO_FILE2):
    data1, data2 = load_files(PATH_TO_FILE1, PATH_TO_FILE2)
    diff = generate_diff_stylish(data1, data2)
    return diff
