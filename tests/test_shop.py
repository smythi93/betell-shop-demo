
from shop.api import checkout, describe, safe_parse

def test_checkout_small():
    assert checkout([1, 2]) == 3

def test_checkout_bulk():
    assert checkout([10] * 12) >= 100

def test_describe():
    assert describe("  Apple ").startswith("item")

def test_parse():
    assert safe_parse("12") == 12
    assert safe_parse("x") is None
