from gendiff.read_files import read_file
from gendiff.formatters.format_gendiff import formatter
from gendiff.tree import diff


def generate_diff(first_file, second_file, format_output='stylish'):
    first_file, second_file = read_file(first_file), read_file(second_file)
    parse_result = diff(first_file, second_file, format_output)
    return formatter(parse_result, format_output)
