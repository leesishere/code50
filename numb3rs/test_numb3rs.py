import sys
import pytest
sys.path.append('/workspaces/21178063/numb3rs')

from validate import numb3rs


def test_True():
    assert validate("255.255.255.255") == True
    assert validate("1.2.3.4") == True

def test_False():
    assert validate("512.512.512.512") == False
    assert validate("1.2.3.1000") == False
    assert validate("cat") == False
