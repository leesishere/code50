import sys
import pytest
sys.path.append('/workspaces/21178063/numb3rs')

from numb3rs import validate


def test_True():
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.4") == True

def test_False():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
    assert validate("256.2.3.1000") == False
    assert validate("1.256.3.1") == False
    assert validate("1.2.256.1") == False
    
