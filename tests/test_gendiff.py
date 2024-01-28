import json
from tests.fixtures.fixtures import diff_format_stylish, diff_format_plain, diff_format_json
from tests.fixtures.standarts.stylish_standart import stylish_standart
from tests.fixtures.standarts.plain_standart import plain_standart

diff_format_stylish = diff_format_stylish
diff_format_plain = diff_format_plain
diff_format_json = diff_format_json


def test_format_stylish(diff_format_stylish):
    a, b = diff_format_stylish
    assert a == stylish_standart
    assert b == stylish_standart


def test_format_plain(diff_format_plain):
    a, b = diff_format_plain
    assert a == plain_standart
    assert b == plain_standart


def test_format_json(diff_format_json):
    a, b = diff_format_json
    standart_json = json.load(
        open('tests/fixtures/standarts/json_standart.json'))
    assert json.loads(a) == standart_json
    assert json.loads(b) == standart_json
