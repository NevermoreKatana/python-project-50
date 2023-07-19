from gendiff.gendiff import get_argument_generation_references
from gendiff.gendiff import generate_diff


def exec_app():
    file1, file2, format = get_argument_generation_references()
    generate_diff(file1, file2, format)
