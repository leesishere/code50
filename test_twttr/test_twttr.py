import sys
import pytest
sys.path.append('/workspaces/21178063/twttr')

from twttr import shorten
def main():
    print("hello")


def test_shorten():
    assert shorten("Jamey) == "Jmy"

if __name__ == "__main__":
    main()
