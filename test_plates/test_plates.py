import sys
import pytest
sys.path.append('/workspaces/21178063/plates')

from plates import is_valid

# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”#

# Numbers cannot be used in the middle of a plate; they must come at the end.
# For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
# CS50P2


def test_is_valid_one_char():
    assert is_valid("J") == False

def test_is_valid_two_char():
    assert is_valid("Ja") == True

def test_without_beginning_alphabetical():
    assert is_valid("01") == False

def test_is_valid_seven_char():
    assert is_valid("SEVEN77") == False

def test_is_valid_number_middle():
    assert is_valid("AAA22A") == False

def test_is_valid_number_last():
    assert is_valid("AAA222") == True

def test_without_beginning_alphabetical_checks():
    assert is_valid("22AAAA") == False

def test_is_invalid_start_with_zero():
    assert is_valid("0AAAAA") == False

def test_is_invalid_alphanumeric_characters():
    assert is_valid("AAAA?A") == False


