from difference_calculator.renderers.standart import generate_diff_dict
from difference_calculator.parser import file_type
from difference_calculator.renderers.plain import generate_diff_plain
from difference_calculator.parser import cmd_gendiff
from difference_calculator.renderers.json import generate_diff_dict_json


def main():
    PATH_TO_FILE1, PATH_TO_FILE2, FORMAT = cmd_gendiff()
    data1, data2 = file_type(PATH_TO_FILE1, PATH_TO_FILE2)
    if FORMAT == 'plain':
        generate_diff_plain(data1, data2)
    elif FORMAT == 'json':
        generate_diff_dict_json(data1, data2)
    else:
        generate_diff_dict(data1, data2)
