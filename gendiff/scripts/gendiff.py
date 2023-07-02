from gendiff.gendiff import diff
import argparse
import json
import yaml


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


def formatter(value, replacer=' ', space_count=1, _lvl=1):
    if isinstance(value, dict):
        result = '{\n'
        for el, val in value.items():
            if el[:1] == "+" or el[:1] == "-":
                result += f'{(replacer * space_count * _lvl)[2:]}{el}:'
                # if val != '':
                result += ' '
            else:
                result += f'{replacer * space_count * _lvl}{el}: '
            result += formatter(val, replacer,
                                space_count, _lvl + 1) + '\n'
        result += replacer * space_count * (_lvl - 1) + '}'
    else:
        value = json.dumps(value)
        result = value.replace('"', '')
    return result


if __name__ == "__main__":
    generate_diff()
