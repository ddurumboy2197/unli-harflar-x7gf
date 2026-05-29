# test_remove_vowels.py
import pytest
from remove_vowels import remove_vowels

def test_remove_vowels():
    assert remove_vowels("Hello World") == "Hll Wrld"
    assert remove_vowels("Python is fun") == "Pythn s fn"
    assert remove_vowels("AEIOU") == ""
    assert remove_vowels("") == ""
    assert remove_vowels("bcdfghjklmnpqrstvwxyz") == "bcdfghjklmnpqrstvwxyz"

def test_remove_vowels_empty_string():
    assert remove_vowels("") == ""

def test_remove_vowels_single_vowel():
    assert remove_vowels("a") == ""
    assert remove_vowels("e") == ""
    assert remove_vowels("i") == ""
    assert remove_vowels("o") == ""
    assert remove_vowels("u") == ""

def test_remove_vowels_multiple_vowels():
    assert remove_vowels("aeiou") == ""
    assert remove_vowels("aeiouAEIOU") == ""
    assert remove_vowels("aeiouAEIOU123") == "123"
