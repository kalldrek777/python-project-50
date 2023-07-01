import pytest
import json

from gendiff.scripts.gendiff import generate_diff


@pytest.fixture
def diff_json_files():
    result_stylish = generate_diff('file1.json', 'file2.json', 'stylish')
    result_plain = generate_diff('file1.json', 'file2.json', 'plain')
    result_json = generate_diff('file1.json', 'file2.json', 'json')
    return result_stylish, result_plain, result_json


@pytest.fixture
def diff_yaml_files():
    result_stylish = generate_diff('filepath1.yml', 'filepath2.yml', 'stylish')
    result_plain = generate_diff('filepath1.yml', 'filepath2.yml', 'plain')
    result_json = generate_diff('filepath1.yml', 'filepath2.yml', 'json')
    return result_stylish, result_plain, result_json


def test_json(diff_json_files):
    a, b, c = diff_json_files
    assert a == ('{\n'
                 '    common: {\n'
                 '      + follow: False\n'
                 '        setting1: Value 1\n'
                 '      - setting2: 200\n'
                 '      - setting3: True\n'
                 '      + setting3: None\n'
                 '      + setting4: blah blah\n'
                 '      + setting5: {\n'
                 '            key5: value5\n'
                 '        }\n'
                 '        setting6: {\n'
                 '            doge: {\n'
                 '              - wow:\n'
                 '              + wow: so much\n'
                 '            }\n'
                 '            key: value\n'
                 '          + ops: vops\n'
                 '        }\n'
                 '    }\n'
                 '    group1: {\n'
                 '      - baz: bas\n'
                 '      + baz: bars\n'
                 '        foo: bar\n'
                 '      - nest: {\n'
                 '            key: value\n'
                 '        }\n'
                 '      + nest: str\n'
                 '    }\n'
                 '  - group2: {\n'
                 '        abc: 12345\n'
                 '        deep: {\n'
                 '            id: 45\n'
                 '        }\n'
                 '    }\n'
                 '  + group3: {\n'
                 '        deep: {\n'
                 '            id: {\n'
                 '                number: 45\n'
                 '            }\n'
                 '        }\n'
                 '        fee: 100500\n'
                 '    }\n'
                 '}')
    assert b == \
           ("Property 'common.follow' was added with value: 'False'\n"
            "Property 'common.setting2' was removed\n"
            "Property 'common.setting3' was updated. From 'True' to 'None'\n"
            "Property 'common.setting4' was added with value: 'blah blah'\n"
            "Property 'common.setting5' was added with value: "
            "[complex value]\n"
            "Property 'common.setting6.doge.wow' was updated. "
            "From '' to 'so much'\n"
            "Property 'common.setting6.ops' was added with value: 'vops'\n"
            "Property 'group1.baz' was updated. From 'bas' to 'bars'\n"
            "Property 'group1.nest' was updated."
            " From [complex value] to 'str'\n"
            "Property 'group2' was removed\n"
            "Property 'group3' was added with value: [complex value]")
    assert json.loads(c) == json.load(open('test_format_json.json'))


def test_yaml(diff_yaml_files):
    a, b, c = diff_yaml_files
    assert a == ('{\n'
                 '    common: {\n'
                 '      + follow: False\n'
                 '        setting1: Value 1\n'
                 '      - setting2: 200\n'
                 '      - setting3: True\n'
                 '      + setting3: None\n'
                 '      + setting4: blah blah\n'
                 '      + setting5: {\n'
                 '            key5: value5\n'
                 '        }\n'
                 '        setting6: {\n'
                 '            doge: {\n'
                 '              - wow:\n'
                 '              + wow: so much\n'
                 '            }\n'
                 '            key: value\n'
                 '          + ops: vops\n'
                 '        }\n'
                 '    }\n'
                 '    group1: {\n'
                 '      - baz: bas\n'
                 '      + baz: bars\n'
                 '        foo: bar\n'
                 '      - nest: {\n'
                 '            key: value\n'
                 '        }\n'
                 '      + nest: str\n'
                 '    }\n'
                 '  - group2: {\n'
                 '        abc: 12345\n'
                 '        deep: {\n'
                 '            id: 45\n'
                 '        }\n'
                 '    }\n'
                 '  + group3: {\n'
                 '        deep: {\n'
                 '            id: {\n'
                 '                number: 45\n'
                 '            }\n'
                 '        }\n'
                 '        fee: 100500\n'
                 '    }\n'
                 '}')

    assert b == \
               ("Property 'common.follow' was added with value: 'False'\n"
            "Property 'common.setting2' was removed\n"
            "Property 'common.setting3' was updated. From 'True' to 'None'\n"
            "Property 'common.setting4' was added with value: 'blah blah'\n"
            "Property 'common.setting5' was added with value: "
            "[complex value]\n"
            "Property 'common.setting6.doge.wow' was updated. "
            "From '' to 'so much'\n"
            "Property 'common.setting6.ops' was added with value: 'vops'\n"
            "Property 'group1.baz' was updated. From 'bas' to 'bars'\n"
            "Property 'group1.nest' was updated."
            " From [complex value] to 'str'\n"
            "Property 'group2' was removed\n"
            "Property 'group3' was added with value: [complex value]")
    assert json.loads(c) == json.load(open('test_format_json.json'))
