import pytest
from gendiff.gendiff import generate_diff


@pytest.fixture
def diff_json_files():
    result_stylish = generate_diff('tests/fixtures/file1.json',
                                   'tests/fixtures/file2.json', 'stylish')
    result_plain = generate_diff('tests/fixtures/file1.json',
                                 'tests/fixtures/file2.json', 'plain')
    result_json = generate_diff('tests/fixtures/file1.json',
                                'tests/fixtures/file2.json', 'json')
    return result_stylish, result_plain, result_json


@pytest.fixture
def diff_yaml_files():
    result_stylish = generate_diff('tests/fixtures/filepath1.yml',
                                   'tests/fixtures/filepath2.yml', 'stylish')
    result_plain = generate_diff('tests/fixtures/filepath1.yml',
                                 'tests/fixtures/filepath2.yml', 'plain')
    result_json = generate_diff('tests/fixtures/filepath1.yml',
                                'tests/fixtures/filepath2.yml', 'json')
    return result_stylish, result_plain, result_json
