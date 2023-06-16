from gendiff import main
import os, sys

# result = os.system('poetry run gendiff file1.json file2.json')
# print(result)


def result():
    parser = main('file1.json', 'file2.json')
    return parser


def test_files():
    # parser = os.system('poetry run gendiff python-project-50/file1.json file2.json')
    print(result)
    parser = result
    print(parser)