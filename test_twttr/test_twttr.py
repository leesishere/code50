import sys
import pytest
sys.path.append('/workspaces/21178063/twttr')

from twttr import shorten

def test_shorten():
    assert shorten("Jamey") == "Jmy"

def test_without_vowel():
    assert shorten("BCDFG") == "BCDFG"

def test_without_capitalized():
    assert shorten("jamey") == "jmy"

def test_without_lowercase():
     assert shorten("JAMEY") == "JMY"

def test_omitting_numbers():
    assert shorten("1") == "1"

def test_error():
    with pytest.raises(TypeError):
        assert shorten(1)

