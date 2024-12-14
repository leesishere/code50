import sys
import pytest
sys.path.append('/workspaces/21178063/plates')

from plates import is_valid

# “All vanity plates must start with at least two letters.”
# “… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”#

# Numbers cannot be used in the middle of a plate; they must come at the end.
# For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
# CS50P2

def test_is_valid_cs_class():
    assert is_valid("CS50") == True

def test_is_invalid_zero_position():
    assert is_valid("CS05") == False

def test_is_invalid_number_middle():
    assert is_valid("CS50P") == False

def test_is_invalid_alphanumeric_characters():
    assert is_valid("PI3.14") == False


def test_is_invalid_seven_char():
    assert is_valid("OUTATIME") == False

def test_is_invalid_start_with_two_char():
    assert is_valid("H") == False

def test_is_valid_two_char():
    assert is_valid("Ja") == True

def test_is_valid_number_last():
    assert is_valid("AAA222") == True

'''
def test_invalid_without_beginning_alphabetical():
    assert is_valid("12AA") == False



def test_is_without_beginning_alphabetical_checks():
    assert is_valid("ABC") == False



def test_invalid_start_with_zero_placement():
    assert is_valid("AAAA01") == False



'''

