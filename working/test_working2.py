import sys
sys.path.append('/workspaces/21178063/working')
from working import convert
import pytest

def main():
    test_wrong_formate()
    test_time()
    test_wrong_hour()
    test_wrong_minute()

def test_wrong_formate()
    with pytest.raises(ValueError):
        convert('9 am - 9 PM')

def test_time()

def test_wrong_hour()

def test_wrong_minute()
