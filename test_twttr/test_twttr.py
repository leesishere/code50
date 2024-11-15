import sys
import pytest
sys.path.append('/workspaces/21178063/twttr')

from twttr import shorten

def test_shorten():
    assert shorten("Jamey") == "Jmy"
    assert shorten("JAMEY") == "Jmy"

def test_error():
    with pytest.raises(TypeError):
        assert shorten(1)

