import twttr
from twttr import shorten

def test_shorten_lowercase():
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"
    assert shorten("aeiou") == ""

def test_shorten_uppercase():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("HELLO") == "HLL"
    assert shorten("AEIOU") == ""

def test_shorten_mixed():
    assert shorten("TwItTeR") == "TwtTR"
    assert shorten("HeLLo") == "HLL"
    assert shorten("aEiOu") == ""

def test_shorten_with_numbers_and_symbols():
    assert shorten("h3ll0!") == "h3ll0!"
    assert shorten("CS50!") == "CS50!"