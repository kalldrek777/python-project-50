import json
import yaml


def read_file(file):
    if file.endswith('.json'):
        extension = 'json'
    else:
        extension = 'yaml'
    result = parse(open(file), extension)
    return result


def parse(file, extension):
    if extension == 'yaml':
        file = yaml.safe_load(file)
    else:
        file = json.load(file)
    return file
