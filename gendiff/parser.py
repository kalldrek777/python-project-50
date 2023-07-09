import argparse
import json
import yaml
from gendiff.formatter import formatter
from gendiff.gendiff import diff


def parse_args():
    parser = argparse.ArgumentParser(description="Compares two"
                                                 " configuration files "
                                                 "and shows a difference.")

    # position arguments
    parser.add_argument("first_file")
    parser.add_argument("second_file")

    # optional arguments
    parser.add_argument("-f", "--format", help="set format "
                                               "of output", default="stylish")

    args = parser.parse_args()
    if args.first_file.endswith('.json'):
        first_file = json.load(open(args.first_file))
    else:
        with open(args.first_file, 'r') as f:
            first_file = yaml.safe_load(f)

    if args.second_file.endswith('.json'):
        second_file = json.load(open(args.second_file))
    else:
        with open(args.second_file, 'r') as f:
            second_file = yaml.safe_load(f)

    parse_result = diff(first_file, second_file, args.format)
    if args.format == "stylish":
        return formatter(parse_result, replacer=' ', space_count=4, _lvl=1)
    elif args.format == "plain":
        return parse_result[:-1]
    elif args.format == "json":
        return json.dumps(parse_result)