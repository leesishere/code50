import sys
import pytest
sys.path.append('/workspaces/21178063/numb3rs')

from validate import numb3rs


def test_():
    assert validate("Jamey") == 100

def test_hello_upper():
    assert value("HELLO") == 0

def test_hello_lower():
    assert value("hello") == 0

def test_hello_mixed():
    assert value("heLLo") == 0

def test_just_start_with_h():
    assert value("howdy") == 20

def test_just_start_with_h_two():
    assert value("hi") == 20
