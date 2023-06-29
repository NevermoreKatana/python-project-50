import json
from difference_calculator.parser.parser import parser


PATH_TO_FILE1 = 'difference_calculator/file1.json'
PATH_TO_FILE2 = 'difference_calculator/file2.json'
PATH_TO_FILE1YMl = 'difference_calculator/file1.yml'
PATH_TO_FILE2YMl = 'difference_calculator/file2.yml'


def gendiff(file1, file2):
    result = dict()
    for i in sorted(file1.keys()):
        if i not in file2:
            result[f'- {i}'] = file1[i]
            del file1[i]
        elif file1[i] == file2.get(i):
            result[f'  {i}'] = file1[i]
            del file1[i], file2[i]
        elif i in file2:
            result[f'- {i}'] = file1[i]
            result[f'+ {i}'] = file2[i]
            del file1[i], file2[i]
    for i in file2:
        result[f"+ {i}"] = file2[i]
        del i
    print(json.dumps(result, indent=2))
    return json.dumps(result, indent=2)


def main():
    parser('difference_calculator/file1.yml',
           'difference_calculator/file2.yml')
    parser('difference_calculator/file1.json',
           'difference_calculator/file2.json')
