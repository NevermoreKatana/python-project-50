from gendiff.gendiff import get_argument_generation_references
from gendiff.gendiff import generate_diff


def main():
    file1, file2, format = get_argument_generation_references()
    diff = generate_diff(file1, file2, format)


if __name__ == '__main__':
    print(main())
