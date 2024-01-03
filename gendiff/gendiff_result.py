import json
from gendiff.formatters.format_plain import format_plain
from gendiff.formatters.format_stylish import stylish


def formatter(parse_result, format):
    if format == "stylish":
        return stylish(parse_result)
    elif format == "plain":
        return format_plain(parse_result)[:-1]
    elif format == "json":
        return format_json(parse_result)


def format_json(val):
    return json.dumps(val, indent=2)
