import json


# def stylish(value, replacer=' ', space_count=1, _lvl=1):
#     if isinstance(value, dict):
#         result = '{\n'
#         for el, val in value.items():
#             if el[:1] == "+" or el[:1] == "-":
#                 result += f'{(replacer * space_count * _lvl)[2:]}{el}:'
#                 # if val != '':
#                 result += ' '
#             else:
#                 result += f'{replacer * space_count * _lvl}{el}: '
#             result += stylish(val, replacer,
#                                 space_count, _lvl + 1) + '\n'
#         result += replacer * space_count * (_lvl - 1) + '}'
#     else:
#         value = json.dumps(value)
#         result = value.replace('"', '')
#     return result
def stylish(value, replacer=' ', space_count=1, _lvl=1):
    if isinstance(value, list):
        result = '{\n'
        for i in value:
            if i['type'] == 'added':
                key = '+ ' + i['key']
                result += f'{(replacer * space_count * _lvl)[2:]}{key}: '
                if isinstance(i['value'], list) or \
                        isinstance(i['value'], dict):
                    result += stylish(i['value'],
                                      replacer, space_count, _lvl + 1) + '\n'
                else:
                    val = json.dumps(i['value']).replace('"', '') + '\n'
                    result += val
            if i['type'] == 'deleted':
                key = '- ' + i['key']
                result += f'{(replacer * space_count * _lvl)[2:]}{key}: '
                if isinstance(i['value'], list) \
                        or isinstance(i['value'], dict):
                    result += stylish(i['value'], replacer,
                                      space_count, _lvl + 1) + '\n'
                else:
                    val = json.dumps(i['value']).replace('"', '') + '\n'
                    result += val
            if i['type'] == 'updated':
                key = '- ' + i['key']
                result += f'{(replacer * space_count * _lvl)[2:]}{key}: '
                if isinstance(i['value1'], list) or \
                        isinstance(i['value1'], dict):
                    result += stylish(i['value1'], replacer,
                                      space_count, _lvl + 1) + '\n'
                else:
                    val = json.dumps(i['value1']).replace('"', '') + '\n'
                    result += val

                key = '+ ' + i['key']
                result += f'{(replacer * space_count * _lvl)[2:]}{key}: '
                if isinstance(i['value2'], list) or \
                        isinstance(i['value2'], dict):
                    result += stylish(i['value2'],
                                      replacer, space_count, _lvl + 1) + '\n'
                else:
                    val = json.dumps(i['value2']).replace('"', '') + '\n'
                    result += val
            if i['type'] == 'saved':
                key = i['key']
                result += f'{replacer * space_count * _lvl}{key}: '
                if isinstance(i['value'], list) or \
                        isinstance(i['value'], dict):
                    result += stylish(i['value'], replacer,
                                      space_count, _lvl + 1) + '\n'
                else:
                    val = json.dumps(i['value']).replace('"', '') + '\n'
                    result += val
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


# def format_plain(dictionary, path=None, list_keys=None):
#     result_str = ""
#     if path is None:
#         path = []
#     if list_keys is None:
#         a, b = find_keys(dictionary, [])
#         list_keys = b
#
#     for k, v in dictionary.items():
#         if k[:1] == "+" or k[:1] == "-":
#             newpath = path + [k[2:]]
#             if list_keys.count(newpath) == 2:
#                 key_path = '.'.join(newpath)
#                 if k[:1] == "-":
#                     if isinstance(v, dict):
#                         result_str += f"Property '{key_path}' was " \
#                                       f"updated. From [complex value]"
#                     else:
#                         v = json.dumps(v).replace('"', "'")
#                         result_str += f"Property '{key_path}' was " \
#                                       f"updated. From {v}"
#
#                 if k[:1] == "+":
#                     if isinstance(v, dict):
#                         result_str += " to [complex value]\n"
#                     else:
#                         v = json.dumps(v).replace('"', "'")
#                         result_str += f" to" \
#                                       f" {v}\n"
#
#             else:
#                 if k[:1] == "-":
#                     key_path = '.'.join(newpath)
#                     result_str += f"Property '{key_path}' was removed\n"
#                 elif k[:1] == "+":
#                     key_path = '.'.join(newpath)
#                     if isinstance(v, dict):
#                         result_str += f"Property '{key_path}' was added" \
#                                       f" with value: [complex value]\n"
#                     else:
#                         v = json.dumps(v).replace('"', "'")
#                         result_str += f"Property '{key_path}' " \
#                                       f"was added with value: {v}\n"
#
#         else:
#             newpath = path + [k]
#             if isinstance(v, dict):
#                 result_str += format_plain(v, path=newpath,
#                                            list_keys=list_keys)
#     return result_str


def format_plain(dictionary, path=None):
    result_str = ""
    if path is None:
        path = []
    if isinstance(dictionary, list):
        for i in dictionary:
            newpath = path + [i['key']]
            if i['type'] == 'saved':
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


def json_format(value):
    result = ""
    if isinstance(value, list):
        for i in value:
            if i['type'] == 'saved':
                if isinstance(i['value'], list):
                    result += json_format(i['value'])
            else:
                result += str(i)
    return result

# def find_keys(dictionary, list_keys, path=None):
#     if path is None:
#         path = []
#     for k, v in dictionary.items():
#         if k[:1] == "+" or k[:1] == "-":
#             k = k[2:]
#         newpath = path + [k]
#         list_keys.append(newpath)
#         if isinstance(v, dict):
#             a, b = find_keys(v, list_keys, newpath)
#             newpath + [a]
#     return k, list_keys
