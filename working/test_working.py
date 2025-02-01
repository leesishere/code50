import sys
import pytest
sys.path.append('/workspaces/21178063/working')

from working import convert


def test_True():
    assert convert("255.255.255.255") == True
   
