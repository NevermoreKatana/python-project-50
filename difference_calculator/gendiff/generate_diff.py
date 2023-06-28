import json

PATH_TO_FILE1 = 'difference_calculator/file1.json'
PATH_TO_FILE2 = 'difference_calculator/file2.json'


def generate_diff(filename1, filename2):
    fn1 = json.load(open(filename1))
    fn2 = json.load(open(filename2))
    result = dict()
    for i in sorted(fn1.keys()):
        if i not in fn2:
            result[f'- {i}'] = fn1[i]
            del fn1[i]
        elif fn1[i] == fn2.get(i):
            result[f'  {i}'] = fn1[i]
            del fn1[i], fn2[i]
        elif i in fn2:
            result[f'- {i}'] = fn1[i]
            result[f'+ {i}'] = fn2[i]
            del fn1[i], fn2[i]
    for i in fn2:
        result[f"+ {i}"] = fn2[i]
        del i
    print(json.dumps(result, indent=2))
    return json.dumps(result, indent=2)


def main():
    generate_diff(PATH_TO_FILE1, PATH_TO_FILE2)
