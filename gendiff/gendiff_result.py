import json
from gendiff.formatter import stylish, format_plain, json_format


def format(parse_result, format_):
    if format_ == "stylish":
        return stylish(parse_result, replacer=' ', space_count=4, _lvl=1)
    elif format_ == "plain":
        return format_plain(parse_result)[:-1]
    elif format_ == "json":
        return json_dumps(parse_result)


def json_dumps(val):
    return json.dumps(json_format(val))
