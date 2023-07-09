import pytest
from gendiff.scripts.gendiff import generate_diff


@pytest.fixture
def diff_json_files():
    result_stylish = generate_diff('tests/test_files/file1.json', 'tests/test_files/file2.json', 'stylish')
    result_plain = generate_diff('tests/test_files/file1.json', 'tests/test_files/file2.json', 'plain')
    result_json = generate_diff('tests/test_files/file1.json', 'tests/test_files/file2.json', 'json')
    return result_stylish, result_plain, result_json


@pytest.fixture
def diff_yaml_files():
    result_stylish = generate_diff('tests/test_files/filepath1.yml', 'tests/test_files/filepath2.yml', 'stylish')
    result_plain = generate_diff('tests/test_files/filepath1.yml', 'tests/test_files/filepath2.yml', 'plain')
    result_json = generate_diff('tests/test_files/filepath1.yml', 'tests/test_files/filepath2.yml', 'json')
    return result_stylish, result_plain, result_json
