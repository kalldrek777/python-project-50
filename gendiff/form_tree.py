

def diff(first_file, second_file, format_name='stylish', path=None):
    key_list = []

    for key in {**first_file, **second_file}.keys():
        key_list.append(key)

    key_list_set = set(key_list)
    key_list = list(key_list_set)
    key_list.sort()

    updated_dict = {}

    for key in key_list:
        if key in first_file:
            if key in second_file:
                if isinstance(first_file[key], dict) and \
                        isinstance(second_file[key], dict):
                    a = diff(first_file[key],
                             second_file[key], format_name)
                    updated_dict[key] = a
                else:
                    if first_file[key] == second_file[key]:
                        updated_dict[key] = first_file[key]
                    elif first_file[key] != second_file[key]:
                        updated_dict['- ' + key] = first_file[key]
                        updated_dict['+ ' + key] = second_file[key]
            else:
                updated_dict['- ' + key] = first_file[key]
        else:
            updated_dict['+ ' + key] = second_file[key]
    return updated_dict
