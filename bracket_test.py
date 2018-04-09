import pytest
from bracket_check import unbalenced

def test_string():
    x = unbalenced('hello world')
    assert x == -1

def test_matched_simple():
    x = unbalenced('{}')
    assert x == -1

def test_matched_mixed():
    x = unbalenced('{{{foo();}}}{}')
    assert x == -1

def test_matched_nested():
    x = unbalenced('{{}{}}')
    assert x == -1

def test_unmatched_open():
    x = unbalenced('{{{}')
    assert x == 0

def test_unmatched_close():
    x = unbalenced('}')
    assert x == 0

def test_unmatched_middle():
    x = unbalenced('{}{foo{}')
    assert x == 2
