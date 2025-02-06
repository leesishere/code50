import sys
sys.path.append('/workspaces/21178063/seasons/')
import pytest

from jar import Jar

def test_action_without_fixtures():
    sc = SuperCool()
    sc.element = 'snow'
    sc.melt()
    assert sc.element == 'water'
    my = Jar()
    print(my.capacity)
    my.deposit(12)
    print(my.size)
    my.withdraw(10)
    print(my.size)
