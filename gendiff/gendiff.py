import json


def diff(first_file, second_file, format_name='stylish', path=None):
    if path is None:
        path = []
    key_list = []

    for key, value in first_file.items():
        key_list.append(key)

    for key, value in second_file.items():
        key_list.append(key)

    key_list_set = set(key_list)
    key_list = list(key_list_set)
    key_list.sort()

    if format_name == "plain":
        result_str = ""

        for key in key_list:
            newpath = path + [key]
            if key in first_file:
                if key in second_file:
                    if isinstance(first_file[key], dict) and \
                            isinstance(second_file[key], dict):
                        a = diff(first_file[key],
                                 second_file[key], format_name, newpath)
                        result_str += a
                    else:
                        if first_file[key] != second_file[key]:
                            key_path = '.'.join(newpath)
                            if isinstance(first_file[key], dict):
                                second_file[key] = json.dumps(
                                    second_file[key]).replace('"', "'")
                                result_str += f"Property '{key_path}' was " \
                                              f"updated. From [complex value]"\
                                              f" to {second_file[key]}\n"
                            elif isinstance(second_file[key], dict):
                                first_file[key] = json.dumps(
                                    first_file[key]).replace('"', "'")
                                result_str += f"Property '{key_path}'" \
                                              f" was updated. From " \
                                              f"{first_file[key]} to" \
                                              f" [complex value]\n"
                            else:
                                first_file[key] = json.dumps(
                                    first_file[key]).replace('"', "'")
                                second_file[key] = json.dumps(
                                    second_file[key]).replace('"', "'")
                                result_str += f"Property '{key_path}' " \
                                              f"was updated. From " \
                                              f"{first_file[key]} to " \
                                              f"{second_file[key]}\n"

                else:
                    key_path = '.'.join(newpath)
                    result_str += f"Property '{key_path}' was removed\n"
            else:
                key_path = '.'.join(newpath)
                if isinstance(second_file[key], dict):
                    result_str += f"Property '{key_path}' " \
                                  f"was added with value: [complex value]\n"
                else:
                    second_file[key] = json.dumps(
                        second_file[key]).replace('"', "'")
                    result_str += f"Property '{key_path}' " \
                                  f"was added with value: {second_file[key]}\n"
        return result_str

    else:

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
