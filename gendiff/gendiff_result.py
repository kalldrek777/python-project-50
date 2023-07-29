import json
from gendiff.formatter import stylish, format_plain, json_output


def format(parse_result, format):
    if format == "stylish":
        return stylish(parse_result, replacer=' ', space_count=4, _lvl=1)
    elif format == "plain":
        return format_plain(parse_result)[:-1]
    elif format == "json":
        return format_json(json_output(parse_result))


def format_json(val):
    return json.dumps(val)
