#! /bin/python
from gendiff.gendiff import generate_diff
from gendiff.parser import parse_args


def main():
    first_file, second_file, format = parse_args()
    parse_result = generate_diff(first_file, second_file, format)
    print(parse_result)


if __name__ == "__main__":
    main()
