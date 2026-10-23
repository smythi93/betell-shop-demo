
from shop.util import normalize, discount, parse

def checkout(prices):
    total = sum(prices)
    return discount(total)

def describe(name):
    label = normalize(name)
    if label.islower():
        return "item " + label
    return "item " + label.lower()

def safe_parse(text):
    try:
        return parse(text)
    except ValueError:
        return None
