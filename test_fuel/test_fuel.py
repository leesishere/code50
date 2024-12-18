import sys
import pytest
sys.path.append('/workspaces/21178063/fuel')

from fuel import convert
from fuel import gauge

# convert expects a str in X/Y format as input, wherein each of X and Y is an integer,
# and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive.
# If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError.
# If Y is 0, then convert should raise a ZeroDivisionError.

def test_shorten():
    assert convert("1/4") == .25

def test_ValueError():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
    convert("three/four")

'''
    3/4
    4/4
    0/4
    4/0 ZeroDivisionError
    three/four ValueError
    1.5/3 ValueError
'''
