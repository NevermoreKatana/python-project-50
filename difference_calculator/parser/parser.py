import yaml
import json


def parser(path_to_file1, path_to_file2):
    from difference_calculator.gendiff.generate_diff import gendiff
    if '.yml' in path_to_file1 or '.yaml' in path_to_file2:
        print('yaml')
        with open(path_to_file1) as file1:
            with open(path_to_file2) as file2:
                fn1 = yaml.safe_load(file1)
                fn2 = yaml.safe_load(file2)
        return gendiff(fn1, fn2)
    print('json')
    fn1 = json.load(open(path_to_file1))
    fn2 = json.load(open(path_to_file2))
    return gendiff(fn1, fn2)


def main():
    parser('difference_calculator/file1.yml',
           'difference_calculator/file2.yml')
    parser('difference_calculator/file1.json',
           'difference_calculator/file2.json')
