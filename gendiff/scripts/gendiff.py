from gendiff.gendiff import generate_diff
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
