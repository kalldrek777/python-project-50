

def diff(dict1, dict2, format_name='stylish', path=None):
    key_list = []

    key_list = sorted(list(dict1.keys() | dict2.keys()))

    # updated_dict = {}
    result = []

    for key in key_list:
        if key in dict1:
            if key in dict2:
                if isinstance(dict1[key], dict) and \
                        isinstance(dict2[key], dict):
                    a = diff(dict1[key],
                             dict2[key], format_name)
                    result.append({
                        'key': key,
                        'type': 'saved',
                        'value': a
                    })
                    # updated_dict[key] = a
                else:
                    if dict1[key] == dict2[key]:
                        result.append({
                            'key': key,
                            'type': 'saved',
                            'value': dict1[key]
                        })
                        # updated_dict[key] = dict1[key]
                    elif dict1[key] != dict2[key]:
                        result.append({
                            'key': key,
                            'type': 'updated',
                            'value1': dict1[key],
                            'value2': dict2[key]
                        })
                        # updated_dict['- ' + key] = dict1[key]
                        # updated_dict['+ ' + key] = dict2[key]
            else:
                result.append({
                    'key': key,
                    'type': 'deleted',
                    'value': dict1[key]
                })
                # updated_dict['- ' + key] = dict1[key]
        else:
            result.append({
                'key': key,
                'type': 'added',
                'value': dict2[key]
            })
            # updated_dict['+ ' + key] = dict2[key]
    return result
