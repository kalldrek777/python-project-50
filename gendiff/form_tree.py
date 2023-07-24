

def diff(first_file, second_file, format_name='stylish', path=None):
    key_list = []

    for key in {**first_file, **second_file}.keys():
        key_list.append(key)

    key_list_set = set(key_list)
    key_list = list(key_list_set)
    key_list.sort()

    # updated_dict = {}
    result = []

    for key in key_list:
        if key in first_file:
            if key in second_file:
                if isinstance(first_file[key], dict) and \
                        isinstance(second_file[key], dict):
                    a = diff(first_file[key],
                             second_file[key], format_name)
                    result.append({
                                'key': key,
                                'type': 'saved',
                                'value': a
                                })
                    # updated_dict[key] = a
                else:
                    if first_file[key] == second_file[key]:
                        result.append({
                                  'key': key,
                                  'type': 'saved',
                                  'value': first_file[key]
                                })
                        # updated_dict[key] = first_file[key]
                    elif first_file[key] != second_file[key]:
                        result.append({
                                  'key': key,
                                  'type': 'updated',
                                  'value1': first_file[key],
                                  'value2': second_file[key]
                                })
                        # updated_dict['- ' + key] = first_file[key]
                        # updated_dict['+ ' + key] = second_file[key]
            else:
                result.append({
                                  'key': key,
                                  'type': 'deleted',
                                  'value': first_file[key]
                                })
                # updated_dict['- ' + key] = first_file[key]
        else:
            result.append({
                                  'key': key,
                                  'type': 'added',
                                  'value': second_file[key]
                                })
            # updated_dict['+ ' + key] = second_file[key]
    return (result)
    return result
