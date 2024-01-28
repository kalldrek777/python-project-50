import pytest
from gendiff.gendiff import generate_diff


@pytest.fixture
def diff_format_stylish():
    result_stylish_json = generate_diff('tests/fixtures/file1.json',
                                        'tests/fixtures/file2.json',
                                        'stylish')
    result_stylish_yaml = generate_diff('tests/fixtures/filepath1.yml',
                                        'tests/fixtures/filepath2.yml',
                                        'stylish')
    return result_stylish_json, result_stylish_yaml


@pytest.fixture
def diff_format_plain():
    result_plain_json = generate_diff('tests/fixtures/file1.json',
                                      'tests/fixtures/file2.json',
                                      'plain')
    result_plain_yaml = generate_diff('tests/fixtures/filepath1.yml',
                                      'tests/fixtures/filepath2.yml',
                                      'plain')
    return result_plain_json, result_plain_yaml


@pytest.fixture
def diff_format_json():
    result_json_json = generate_diff('tests/fixtures/file1.json',
                                     'tests/fixtures/file2.json',
                                     'json')
    result_json_yaml = generate_diff('tests/fixtures/filepath1.yml',
                                     'tests/fixtures/filepath2.yml',
                                     'json')

    return result_json_json, result_json_yaml
