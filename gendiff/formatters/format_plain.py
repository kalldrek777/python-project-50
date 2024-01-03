import json


def format_plain(data, path=None):
    result_str = ""
    if path is None:
        path = []
    for item in data:
        newpath = path + [item['key']]
        if item['type'] == 'nested':
            if isinstance(item['value'], list):
                result_str += format_plain(item['value'], newpath)
        if item['type'] == 'added':
            key_path = '.'.join(newpath)
            if isinstance(item['value'], dict):
                result_str += f"Property '{key_path}' was added" \
                              f" with value: [complex value]\n"
            else:
                value = dumps_to_json(item['value'])
                result_str += f"Property '{key_path}' " \
                              f"was added with value: {value}\n"
        if item['type'] == 'deleted':
            key_path = '.'.join(newpath)
            result_str += f"Property '{key_path}' was removed\n"
        if item['type'] == 'updated':
            key_path = '.'.join(newpath)
            if isinstance(item['value1'], dict):
                result_str += f"Property '{key_path}' was " \
                              f"updated. From [complex value]"
            else:
                value = dumps_to_json(item['value1'])
                result_str += f"Property '{key_path}' was " \
                              f"updated. From {value}"

            if isinstance(item['value2'], dict):
                result_str += " to [complex value]\n"
            else:
                value = dumps_to_json(item['value2'])
                result_str += f" to" \
                              f" {value}\n"
    return result_str


def dumps_to_json(data):
    return json.dumps(data).replace('"', "'")
