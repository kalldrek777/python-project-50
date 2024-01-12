import json

REPLACER = ' '
SPACE_COUNT = 4


def format_stylish(value, replacer=REPLACER, space_count=SPACE_COUNT, depth=1):
    if isinstance(value, list):
        result = '{\n'
        for item in value:
            key = item['key']
            if item['type'] == 'added':
                value = exam(item['value'], depth)
                result += f'{(replacer * space_count * depth)[2:]}+ {key}: {value}'
            if item['type'] == 'deleted':
                value = exam(item['value'], depth)
                result += f'{(replacer * space_count * depth)[2:]}- {key}: {value}'
            if item['type'] == 'updated':
                value1 = exam(item['value1'], depth)
                value2 = exam(item['value2'], depth)
                result += f'{(replacer * space_count * depth)[2:]}- {key}: {value1}'
                result += f'{(replacer * space_count * depth)[2:]}+ {key}: {value2}'
            if item['type'] == 'nested':
                value = exam(item['value'], depth)
                result += f'{(replacer * space_count * depth)}{key}: {value}'

        result += replacer * space_count * (depth - 1) + '}'
    else:
        result = format_dic(value, replacer, space_count, depth)

    return result


def format_dic(value, replacer=REPLACER, space_count=SPACE_COUNT, depth=1):
    if isinstance(value, dict):
        result = '{\n'
        for el, val in value.items():
            result += f'{replacer * space_count * depth}{el}: '
            result += format_stylish(val, replacer,
                                     space_count, depth + 1) + '\n'
        result += replacer * space_count * (depth - 1) + '}'
    else:
        value = json.dumps(value)
        result = value.replace('"', '')
    return result


def exam(value, depth):
    if isinstance(value, list) or isinstance(value, dict):
        result = format_stylish(value,
                                REPLACER, SPACE_COUNT, depth + 1) + '\n'
    else:
        val = json.dumps(value).replace('"', '') + '\n'
        result = val
    return result
