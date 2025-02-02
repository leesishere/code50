import sys
sys.path.append('/workspaces/21178063/um')
from um import count
import pytest

def main():
    test_count_five_um()
    #test_count_no_um()

def test_count_five_um():
    assert count("I , Um, love talking um but what I, UM don't like to do is day Um a lot uM") == 5

def test_count_no_um():
    assert count("I , yummy, love talking ummma but what I, UMs don't like to do is day Uma a lot uMe") == 0

if __name__ == "__main__":
    main()
    exit_code = pytest.main()
    sys.exit(exit_code)
