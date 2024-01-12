from gendiff.formatters.format_plain import format_plain
from gendiff.formatters.format_stylish import format_stylish
from gendiff.formatters.format_json import format_json


def formatter(parse_result, format):
    if format == "stylish":
        return format_stylish(parse_result)
    elif format == "plain":
        return format_plain(parse_result)[:-1]
    elif format == "json":
        return format_json(parse_result)

