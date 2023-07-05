from difference_calculator.gendiff.generate_diff import generate_diff_dict
from difference_calculator.gendiff.parser import pars
from difference_calculator.formatting.plain_format import generate_diff_plain
from difference_calculator.cmd_gendiff import cmd_gendiff
from difference_calculator.formatting.json_format import generate_diff_dict_json


def main():
    PATH_TO_FILE1, PATH_TO_FILE2, FORMAT = cmd_gendiff()
    data1, data2 = pars(PATH_TO_FILE1, PATH_TO_FILE2)
    if FORMAT == 'plain':
        generate_diff_dict(data1, data2)
        generate_diff_plain(data1, data2)
    if FORMAT == 'json':
        generate_diff_dict_json(data1, data2)

    else:
        generate_diff_dict_json(data1, data2)
