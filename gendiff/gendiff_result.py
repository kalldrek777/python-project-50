import json
from gendiff.formatter import formatter, format_plain


def gendiff_result(parse_result, format_):
    if format_ == "stylish":
        return formatter(parse_result, replacer=' ', space_count=4, _lvl=1)
    elif format_ == "plain":
        return format_plain(parse_result)[:-1]
    elif format_ == "json":
        return json.dumps(parse_result)
