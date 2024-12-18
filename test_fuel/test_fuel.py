import sys
import pytest
sys.path.append('/workspaces/21178063/fuel')

from fuel import convert
from fuel import gauge

# convert expects a str in X/Y format as input, wherein each of X and Y is an integer,
# and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive.
# If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError.
# If Y is 0, then convert should raise a ZeroDivisionError.

def test_convert():
    assert convert("1/4") == 25
    assert convert("3/4") == 75
    assert convert("4/4") == 1
    assert convert("0/4") == 0


def test_gauge():
    assert gauge(.25) == '25%'
    assert gauge(.75) == '75%'
    assert gauge(1) == 'F'
    assert gauge(0) == 'E'

def test_ValueError():
    with pytest.raises(ValueError):
        assert convert("three/four")
        assert convert("1.5/3")

def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        assert convert("4/0")





'''
    3/4
    4/4
    0/4
    4/0 ZeroDivisionError
    three/four ValueError
    1.5/3 ValueError
'''
