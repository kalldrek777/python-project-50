import json


def format_plain(data, path=None):
    result = []
    if path is None:
        path = []
    for item in data:
        newpath = path + [item['key']]
        key_path = '.'.join(newpath)
        if item['type'] == 'nested':
            result.append(nested(item, newpath))
        if item['type'] == 'added':
            result.append(added(item, key_path))
        if item['type'] == 'deleted':
            result.append(f"Property '{key_path}' was removed")
        if item['type'] == 'updated':
            result.append(updated(item, key_path))
    result = [item for item in result if item != '']
    return '\n'.join(result)

def updated(item, key_path):
    if isinstance(item['value1'], dict):
        value_from = f"Property '{key_path}' was " \
                     f"updated. From [complex value]"
    else:
        value = dumps_to_json(item['value1'])
        value_from = f"Property '{key_path}' was " \
                     f"updated. From {value}"

    if isinstance(item['value2'], dict):
        value_to = " to [complex value]"
    else:
        value = dumps_to_json(item['value2'])
        value_to = f" to {value}"
    return value_from + value_to


def added(item, key_path):
    if isinstance(item['value'], dict):
        result = f"Property '{key_path}' was added" \
                 f" with value: [complex value]"
    else:
        value = dumps_to_json(item['value'])
        result = f"Property '{key_path}' " \
                 f"was added with value: {value}"
    return result


def nested(item, newpath):
    if isinstance(item['value'], list):
        result = format_plain(item['value'], newpath)
        return result
    else:
        return ''


def dumps_to_json(data):
    return json.dumps(data).replace('"', "'")
