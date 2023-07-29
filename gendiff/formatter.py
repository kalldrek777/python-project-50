import json


def stylish(value, replacer=' ', space_count=1, _lvl=1):
    if isinstance(value, list):
        result = '{\n'
        for i in value:
            if i['type'] == 'added':
                key = '+ ' + i['key']
                result += f'{(replacer * space_count * _lvl)[2:]}{key}: '
                result += exam(i['value'], replacer, space_count, _lvl)
            if i['type'] == 'deleted':
                key = '- ' + i['key']
                result += f'{(replacer * space_count * _lvl)[2:]}{key}: '
                result += exam(i['value'], replacer, space_count, _lvl)
            if i['type'] == 'updated':
                key = '- ' + i['key']
                result += f'{(replacer * space_count * _lvl)[2:]}{key}: '
                result += exam(i['value1'], replacer, space_count, _lvl)
                key = '+ ' + i['key']
                result += f'{(replacer * space_count * _lvl)[2:]}{key}: '
                result += exam(i['value2'], replacer, space_count, _lvl)
            if i['type'] == 'nested':
                key = i['key']
                result += f'{replacer * space_count * _lvl}{key}: '
                result += exam(i['value'], replacer, space_count, _lvl)
        result += replacer * space_count * (_lvl - 1) + '}'
    elif isinstance(value, dict):
        result = '{\n'
        for el, val in value.items():
            result += f'{replacer * space_count * _lvl}{el}: '
            result += stylish(val, replacer,
                              space_count, _lvl + 1) + '\n'
        result += replacer * space_count * (_lvl - 1) + '}'
    else:
        value = json.dumps(value)
        result = value.replace('"', '')

    return result


def format_plain(dictionary, path=None):
    result_str = ""
    if path is None:
        path = []
    if isinstance(dictionary, list):
        for i in dictionary:
            newpath = path + [i['key']]
            if i['type'] == 'nested':
                if isinstance(i['value'], list):
                    result_str += format_plain(i['value'], newpath)
            if i['type'] == 'added':
                key_path = '.'.join(newpath)
                if isinstance(i['value'], dict):
                    result_str += f"Property '{key_path}' was added" \
                                  f" with value: [complex value]\n"
                else:
                    v = json.dumps(i['value']).replace('"', "'")
                    result_str += f"Property '{key_path}' " \
                                  f"was added with value: {v}\n"
            if i['type'] == 'deleted':
                key_path = '.'.join(newpath)
                result_str += f"Property '{key_path}' was removed\n"
            if i['type'] == 'updated':
                key_path = '.'.join(newpath)
                if isinstance(i['value1'], dict):
                    result_str += f"Property '{key_path}' was " \
                                  f"updated. From [complex value]"
                else:
                    v = json.dumps(i['value1']).replace('"', "'")
                    result_str += f"Property '{key_path}' was " \
                                  f"updated. From {v}"

                if isinstance(i['value2'], dict):
                    result_str += " to [complex value]\n"
                else:
                    v = json.dumps(i['value2']).replace('"', "'")
                    result_str += f" to" \
                                  f" {v}\n"
    return result_str


def json_output(value):
    result = ""
    if isinstance(value, list):
        for i in value:
            if i['type'] == 'nested':
                if isinstance(i['value'], list):
                    result += json_output(i['value'])
            else:
                result += str(i)
    return result


def exam(value, replacer, space_count, _lvl):
    if isinstance(value, list) or isinstance(value, dict):
        result = stylish(value,
                         replacer, space_count, _lvl + 1) + '\n'
    else:
        val = json.dumps(value).replace('"', '') + '\n'
        result = val
    return result
