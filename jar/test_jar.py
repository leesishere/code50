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


def test_withdraw_too_much():
    with pytest.raises(ValueError, match="No more Cookies left!"):
        my = Jar()
        my.withdraw(100)

def test_deposit_too_much():
    with pytest.raises(ValueError, match="Jar is full!"):
        my = Jar()
        my.deposit(100)

