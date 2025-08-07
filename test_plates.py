import plates
from plates import is_valid

def test_valid():
    assert is_valid("CS50") is True
    assert is_valid("AB1234") is True
    assert is_valid("XY123") is True

def test_too_short_or_long():
    assert is_valid("A") is False
    assert is_valid("ABCDEFG") is False

def test_starts_with_two_letters():
    assert is_valid("1CS50") is False
    assert is_valid("C150") is False

def test_numbers_middle():
    assert is_valid("CS50CS") is False
    assert is_valid("CS05") is False

def test_first_number_zero():
    assert is_valid("CS01") is False

def test_non_alphanumeric():
    assert is_valid("CS 50") is False
    assert is_valid("CS.50") is False
    assert is_valid("CS-50") is False