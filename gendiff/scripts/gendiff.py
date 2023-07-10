from gendiff.gendiff import generate_diff
import json
import yaml
from gendiff.read_files import read_file
from gendiff.formatter import formatter
from gendiff.parser import parse_args


def main(*args):
    if args:
        first_file, second_file, format_ = args[0], args[1], args[2]
        parse_result = generate_diff(first_file, second_file, format_)
        return parse_result
    else:
        first_file, second_file, format_ = parse_args()
        parse_result = generate_diff(first_file, second_file, format_)
        print(parse_result)


if __name__ == "__main__":
    main()
