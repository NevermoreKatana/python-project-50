import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument("filename", metavar='first_file')
    parser.add_argument("filename", metavar='second_file')

    args = parser.parse_args()
    print(args.accumulate(args.integers))
