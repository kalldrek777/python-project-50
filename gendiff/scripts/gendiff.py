import argparse
import json
import yaml


def main(*args):
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

        if args[2] == "plain":
            return result_format_flag(first_file, second_file)
        elif args[2] == "json":
            return json.dumps(result(first_file, second_file))
        elif args[2] == "stylish":
            parse_result = result(first_file, second_file)
            return generate_diff(parse_result, replacer=' ', space_count=4, _lvl=1)
    else:
        return parse_args()


def parse_args():
    parser = argparse.ArgumentParser(description="Compares two"
                                                 " configuration files "
                                                 "and shows a difference.")

    # position arguments
    parser.add_argument("first_file")
    parser.add_argument("second_file")

    # optional arguments
    parser.add_argument("-f", "--format", help="set format of output", default="stylish")

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
    if args.format == "stylish":
        parse_result = result(first_file, second_file)
        return generate_diff(parse_result, replacer=' ', space_count=4, _lvl=1)
    elif args.format == "plain":
        return result_format_flag(first_file, second_file)[:-2]
    elif args.format == "json":
        return json.dumps(result(first_file, second_file))
        # return result(first_file, second_file)


def result(first_file, second_file):
    key_list = []

    for key, value in first_file.items():
        key_list.append(key)

    for key, value in second_file.items():
        key_list.append(key)

    key_list_set = set(key_list)
    key_list = list(key_list_set)
    key_list.sort()

    updated_dict = {}

    for key in key_list:
        if key in first_file:
            if key in second_file:
                if isinstance(first_file[key], dict) and isinstance(second_file[key], dict):
                    a = result(first_file[key], second_file[key])
                    updated_dict[key] = a
                else:
                    if first_file[key] == second_file[key]:
                        updated_dict[key] = first_file[key]
                    elif first_file[key] != second_file[key]:
                        updated_dict['- ' + key] = first_file[key]
                        updated_dict['+ ' + key] = second_file[key]
            else:
                updated_dict['- ' + key] = first_file[key]
        else:
            updated_dict['+ ' + key] = second_file[key]

    return updated_dict


def result_format_flag(first_file, second_file, path=None):
    if path is None:
        path = []
    key_list = []

    for key, value in first_file.items():
        key_list.append(key)

    for key, value in second_file.items():
        key_list.append(key)

    key_list_set = set(key_list)
    key_list = list(key_list_set)
    key_list.sort()

    result_str = ""

    for key in key_list:
        newpath = path + [key]
        if key in first_file:
            if key in second_file:
                if isinstance(first_file[key], dict) and isinstance(second_file[key], dict):
                    a = result_format_flag(first_file[key], second_file[key], newpath)
                    result_str += a
                else:
                    if first_file[key] != second_file[key]:
                        key_path = '.'.join(newpath)
                        if isinstance(first_file[key], dict):
                            result_str += f"Property '{key_path}' was updated. From [complex value] to '{second_file[key]}'\n"
                        elif isinstance(second_file[key], dict):
                            result_str += f"Property '{key_path}' was updated. From '{first_file[key]}' to [complex value]\n"
                        else:
                            result_str += f"Property '{key_path}' was updated. From '{first_file[key]}' to '{second_file[key]}'\n"


            else:
                key_path = '.'.join(newpath)
                result_str += f"Property '{key_path}' was removed\n"
        else:
            key_path = '.'.join(newpath)
            if isinstance(second_file[key], dict):
                result_str += f"Property '{key_path}' was added with value: [complex value]\n"
            else:
                result_str += f"Property '{key_path}' was added with value: '{second_file[key]}'\n"
    return result_str


def generate_diff(value, replacer=' ', space_count=1, _lvl=1):
    if isinstance(value, dict):
        result = '{\n'
        for el, val in value.items():
            if el[:1] == "+" or el[:1] == "-":
                result += f'{(replacer * space_count * _lvl)[2:]}{el}:'
                if val != '':
                    result += ' '
            else:
                result += f'{replacer * space_count * _lvl}{el}: '  # key to result str
            result += generate_diff(val, replacer, space_count, _lvl + 1) + '\n'  # value to result str
        result += replacer * space_count * (_lvl - 1) + '}'
    else:
        result = str(value)
    return result


if __name__ == "__main__":
    main()
