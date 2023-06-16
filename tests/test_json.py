import pytest

from gendiff.scripts.gendiff import main
import os, sys

# result = os.system('poetry run gendiff file1.json file2.json')
# print(result)


@pytest.fixture
def result():
    result = main('file1.json', 'file2.json')
    return result


def test_files(result):
    assert result == "{\n  - follow: False\n    host: hexlet.io\n  - proxy: 123.234.53.22\n  - timeout: 50\n\
  + timeout: 20\n  + verbose: True\n}\n"