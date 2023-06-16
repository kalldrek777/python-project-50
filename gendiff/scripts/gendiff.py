import argparse
import json


def main(*args):
    if args:
        print(777)
        first_file = json.load(open(args[0]))
        second_file = json.load(open(args[1]))
        return result(first_file, second_file)
    else:
        return parse_args()


def parse_args():
    parser = argparse.ArgumentParser(description="Compares two"
                                                 " configuration files "
                                                 "and shows a difference.")

    # position arguments
    parser.add_argument("first_file")
    parser.add_argument("second_file")

    # optional arguments
    parser.add_argument("-f", "--format", help="set format of output")

    args = parser.parse_args()
    first_file = json.load(open(args.first_file))
    second_file = json.load(open(args.second_file))
    parse_result = result(first_file, second_file)

    return parse_result


def result(first_file, second_file):
    key_list = []

    for key, value in first_file.items():
        key_list.append(key)

    for key, value in second_file.items():
        key_list.append(key)

    key_list_set = set(key_list)
    key_list = list(key_list_set)
    key_list.sort()

    result = "{\n"

    for key in key_list:
        if key in first_file:
            if key in second_file:
                if first_file[key] == second_file[key]:
                    result += "    " + key + ": " + str(first_file[key]) + "\n"
                    print(key + ": " + str(first_file[key]))
                elif first_file[key] != second_file[key]:
                    result += "  " + '- ' + key + ": " + str(
                        first_file[key]) + "\n" + "  " + '+ ' + \
                              key + ": " + str(
                        second_file[key]) + "\n"
                    print('- ' + key + ": " + str(first_file[key]))
                    print('+ ' + key + ": " + str(second_file[key]))
            else:
                result += "  " + '- ' + key + ": " + \
                          str(first_file[key]) + "\n"
                print('- ' + key + ": " + str(first_file[key]))
        else:
            result += "  " + '+ ' + key + ": " + str(second_file[key]) + "\n"
            print('+ ' + key + ": " + str(second_file[key]))

    result += "}\n"
    print(result)
    return result


if __name__ == "__main__":
    main()
