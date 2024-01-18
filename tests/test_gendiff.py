import json
from tests.fixtures.fixtures import diff_json_files, diff_yaml_files
from tests.fixtures.standarts.stylish_standart import stylish_standart
from tests.fixtures.standarts.plain_standart import plain_standart

diff_json_files = diff_json_files
diff_yaml_files = diff_yaml_files


def test_json(diff_json_files):
    a, b, c = diff_json_files
    assert a == stylish_standart
    assert b == plain_standart

    assert (json.loads(c) == json.load(
        open('tests/fixtures/standarts/json_standart.json')))


def test_yaml(diff_yaml_files):
    a, b, c = diff_yaml_files
    assert a == stylish_standart
    assert b == plain_standart
    assert (json.loads(c) == json.load(
        open('tests/fixtures/standarts/json_standart.json')))
