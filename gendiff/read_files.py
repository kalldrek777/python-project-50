import json
import yaml


def read_file(data):
    if data.endswith('.json'):
        extension = 'json'
    elif data.endswith('.yaml') or data.endswith('.yml'):
        extension = 'yaml'
    else:
        raise 'Wrong format. Gendiff work with .yaml, .yml, .json data'
    result = parse(open(data), extension)
    return result


def parse(data, extension):
    if extension == 'yaml':
        data = yaml.safe_load(data)
    elif extension == 'json':
        data = json.load(data)
    return data
