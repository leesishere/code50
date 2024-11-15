import sys
import pytest
sys.path.append('/workspaces/21178063/twttr')

from twttr import shorten

def test_shorten():
    assert shorten("Jamey") == "Jmy"

def without_vowel():
    assert shorten("ABCDFG") == "ABCDFG"

def without_capitalized():
    assert shorten("jamey") == "jmy"

def without_lowercase():
     assert shorten("JAMEY") == "JMY"

def test_error():
    with pytest.raises(TypeError):
        assert shorten(1)

