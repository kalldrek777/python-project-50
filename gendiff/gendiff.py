from gendiff.read_files import read_file
from gendiff.gendiff_result import formatter
from gendiff.form_tree import diff


def generate_diff(first_file, second_file, format_output='stylish'):
    first_file, second_file = read_file(first_file), read_file(second_file)
    parse_result = diff(first_file, second_file, format_output)
    return formatter(parse_result, format_output)
