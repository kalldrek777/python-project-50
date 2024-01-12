import json
import yaml


def read_file(file):
    if file.endswith('.json'):
        extension = 'json'
    elif file.endswith('.yaml') or file.endswith('.yml'):
        extension = 'yaml'
    else:
        raise 'Wrong format. Gendiff work with .yaml, .yml, .json file'
    result = parse(open(file), extension)
    return result


def parse(file, extension):
    if extension == 'yaml':
        file = yaml.safe_load(file)
    else:
        file = json.load(file)
    return file
