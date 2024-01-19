REPLACER = ' '
SPACE_COUNT = 4


def format_stylish(list_of_nodes, replacer=REPLACER,
                   space_count=SPACE_COUNT, depth=1):
    if isinstance(list_of_nodes, list):
        result = ['{']
        indent = replacer * space_count * depth
        for node in list_of_nodes:
            key = node['key']
            if node['type'] == 'added':
                result.append(
                    f'{indent[2:]}+ {key}: {to_str(node["value"], depth)}'
                )
            if node['type'] == 'deleted':
                result.append(
                    f'{(indent)[2:]}- {key}: {to_str(node["value"], depth)}'
                )
            if node['type'] == 'updated':
                result.extend([
                    f'{(indent)[2:]}- {key}: {to_str(node["value1"], depth)}',
                    f'{(indent)[2:]}+ {key}: {to_str(node["value2"], depth)}'
                ])
            if node['type'] == 'nested':
                result.append(
                    f'{(indent)}{key}: {to_str(node["value"], depth)}'
                )

        result.append(replacer * space_count * (depth - 1) + '}')
    else:
        result = format_dic(list_of_nodes, replacer, space_count, depth)

    return '\n'.join(result)


def format_dic(value, replacer=REPLACER, space_count=SPACE_COUNT, depth=1):
    if isinstance(value, dict):
        result = ['{']
        for el, val in value.items():
            result.append(
                f'{replacer * space_count * depth}{el}: '
                f'{(format_stylish(val, replacer, space_count, depth + 1))}'
            )
        result.append(f'{replacer * space_count * (depth - 1)}' + '}')
    else:
        result = [to_str(value, depth)]
    return result


def to_str(data, depth):
    if isinstance(data, list) or isinstance(data, dict):
        result = format_stylish(data,
                                REPLACER, SPACE_COUNT, depth + 1)
        return result
    elif type(data) is bool:
        return str(data).lower()
    elif data is None:
        return 'null'
    else:
        return str(data)
