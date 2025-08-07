import bank
from bank import value

def test_hello():
    assert value("hello") == 0
    assert value("Hello, friend") == 0

def test_h():
    assert value("hi") == 20
    assert value("hey there") == 20
    assert value("How are you?") == 20

def test_other():
    assert value("good morning") == 100
    assert value("what's up?")