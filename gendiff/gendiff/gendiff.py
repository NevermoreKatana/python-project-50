from gendiff.renderers.standart import generate_dif
from gendiff.parser import file_type
from gendiff.renderers.plain import generate_diff_plain
from gendiff.parser import cmd_gendiff
from gendiff.renderers.json import generate_diff_dict_json


def main():
    PATH_TO_FILE1, PATH_TO_FILE2, FORMAT = cmd_gendiff()
    data1, data2 = file_type(PATH_TO_FILE1, PATH_TO_FILE2)
    if FORMAT == 'plain':
        generate_diff_plain(data1, data2)
    elif FORMAT == 'json':
        generate_diff_dict_json(data1, data2)
    else:
        d = generate_dif(data1, data2)
        print(d)


def generate_diff(PATH_TO_FILE1, PATH_TO_FILE2):
    data1, data2 = file_type(PATH_TO_FILE1, PATH_TO_FILE2)
    return generate_dif(data1, data2)
