from gendiff.scripts.gendiff import main as parse_main
import os, sys

# result = os.system('poetry run gendiff file1.json file2.json')
# print(result)


def main():
    result = parse_main('file1.json', 'file2.json')
    # result = os.system('poetry run snake file1.json file2.json')
    print(result)
    c = '''{
  - follow: False
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: True
}
'''
    "{\n  - follow: False\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n\
  + timeout: 20\n  + verbose: True\n}"
    print(c)
    return result



# def test_files():
#     # parser = os.system('poetry run gendiff python-project-50/file1.json file2.json')
#     print(result)
#     parser = result
#     print(parser)