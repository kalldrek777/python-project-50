import json
import yaml


def read_file(file):
    if file.endswith('.json'):
        file = json.load(open(file))
    else:
        with open(file, 'r') as f:
            file = yaml.safe_load(f)

    return file
