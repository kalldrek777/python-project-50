import json


replacer = ' '
space_count = 4
_lvl = 1


def stylish(value, replacer=replacer, space_count=space_count, _lvl=_lvl):
    if isinstance(value, list):
        result = '{\n'
        for item in value:
            if item['type'] == 'added':
                key = '+ ' + item['key']
                result += f'{(replacer * space_count * _lvl)[2:]}{key}: '
                result += exam(item['value'], _lvl)
            if item['type'] == 'deleted':
                key = '- ' + item['key']
                result += f'{(replacer * space_count * _lvl)[2:]}{key}: '
                result += exam(item['value'], _lvl)
            if item['type'] == 'updated':
                key = '- ' + item['key']
                result += f'{(replacer * space_count * _lvl)[2:]}{key}: '
                result += exam(item['value1'], _lvl)
                key = '+ ' + item['key']
                result += f'{(replacer * space_count * _lvl)[2:]}{key}: '
                result += exam(item['value2'], _lvl)
            if item['type'] == 'nested':
                key = item['key']
                result += f'{replacer * space_count * _lvl}{key}: '
                result += exam(item['value'], _lvl)
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


def exam(value, _lvl):
    if isinstance(value, list) or isinstance(value, dict):
        result = stylish(value,
                         replacer, space_count, _lvl + 1) + '\n'
    else:
        val = json.dumps(value).replace('"', '') + '\n'
        result = val
    return result