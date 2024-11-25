import sys
import pytest
sys.path.append('/workspaces/21178063/plates')

from plates import is_valid

# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”#

# Numbers cannot be used in the middle of a plate; they must come at the end.
# For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
# CS50P2


def is_valid():
    assert value("Ja") == True

