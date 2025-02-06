import sys
sys.path.append('/workspaces/21178063/seasons/')
import pytest

from jar import Jar

def test_get_incorrect_format():
    with pytest.raises(SystemExit):
        assert get_minutes('January 1, 1999')
