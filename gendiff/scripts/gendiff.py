from gendiff.gendiff import diff
import json
import yaml
from gendiff.formatter import formatter
from gendiff.parser import parse_args


def generate_diff(*args):
    if args:
        if args[0].endswith('.json'):
            first_file = json.load(open(args[0]))
        else:
            with open(args[0], 'r') as f:
                first_file = yaml.safe_load(f)

        if args[1].endswith('.json'):
            second_file = json.load(open(args[1]))
        else:
            with open(args[1], 'r') as f:
                second_file = yaml.safe_load(f)

        args = list(args)
        if len(args) < 3:
            args.append("stylish")
        parse_result = diff(first_file, second_file, args[2])

        if args[2] == "stylish":
            return formatter(parse_result, replacer=' ', space_count=4, _lvl=1)
        elif args[2] == "plain":
            return parse_result[:-1]
        elif args[2] == "json":
            return json.dumps(parse_result)
    else:
        print(parse_args())


if __name__ == "__main__":
    generate_diff()
