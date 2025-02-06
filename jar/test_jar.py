import sys
sys.path.append('/workspaces/21178063/seasons/')
import pytest

from jar import Jar

def test_action_without_fixtures():
    my = Jar()
    my.capacity == 12
    my.deposit(12)
    my.size == 12
    my.withdraw(10)
    my.size == 2

def test_whatever():
    try:
        my = Jar()
    except ValueError as exc:
        pytest.fail(exc, pytrace=True)
