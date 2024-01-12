

def diff(dict1, dict2, format_name='stylish'):

    key_list = sorted(list(dict1.keys() | dict2.keys()))

    result = []

    for key in key_list:
        if key in dict1 and key in dict2:
            result.append(flatten(dict1[key], dict2[key], key, format_name))

        if key in dict1 and key not in dict2:
            result.append({
                'key': key,
                'type': 'deleted',
                'value': dict1[key]
            })

        if key in dict2 and key not in dict1:
            result.append({
                'key': key,
                'type': 'added',
                'value': dict2[key]
            })
    return result


def flatten(value1, value2, key, format_name):
    if isinstance(value1, dict) and \
            isinstance(value2, dict):
        a = diff(value1,
                 value2, format_name)
        result = {
            'key': key,
            'type': 'nested',
            'value': a
        }
    else:
        if value1 == value2:
            result = {
                'key': key,
                'type': 'nested',
                'value': value1
            }
        elif value1 != value2:
            result = {
                'key': key,
                'type': 'updated',
                'value1': value1,
                'value2': value2
            }
    return result
