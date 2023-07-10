import json
import yaml


def read_file(first_file, second_file):
    if first_file.endswith('.json'):
        first_file = json.load(open(first_file))
    else:
        with open(first_file, 'r') as f:
            first_file = yaml.safe_load(f)

    if second_file.endswith('.json'):
        second_file = json.load(open(second_file))
    else:
        with open(second_file, 'r') as f:
            second_file = yaml.safe_load(f)
    # if isinstance(args[0], list):
    #     if len(args[0]) < 3:
    #         args[0].append("stylish")
    #     if args[0][0].endswith('.json'):
    #         first_file = json.load(open(args[0][0]))
    #     else:
    #         with open(args[0][0], 'r') as f:
    #             first_file = yaml.safe_load(f)
    #
    #     if args[0][1].endswith('.json'):
    #         second_file = json.load(open(args[0][1]))
    #     else:
    #         with open(args[0][1], 'r') as f:
    #             second_file = yaml.safe_load(f)
    # else:
    #     if args[0].first_file.endswith('.json'):
    #         first_file = json.load(open(args.first_file))
    #     else:
    #         with open(args[0].first_file, 'r') as f:
    #             first_file = yaml.safe_load(f)
    #
    #     if args[0].second_file.endswith('.json'):
    #         second_file = json.load(open(args.second_file))
    #     else:
    #         with open(args[0].second_file, 'r') as f:
    #             second_file = yaml.safe_load(f)

    return first_file, second_file
