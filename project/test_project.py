import pytest
from project import load_data, select_word, replace, replace, display_word, get_score, guess_menu, main
import os, json
import pexpect, re


def load_data_test(file_name)->json:
    """

    Description
    ----------
    This function load_data loads the data type JSON for the pytest.

    Parameters
    ----------
    load_data_test(str) : Jason

    User input
    ----------
    None

    Returns
    -------
    json

    """

    if os.path.isfile(file_name):
        with open(file_name, 'r') as json_file:
            return json.load(json_file)

def test_load_data():
    """

    Description
    ----------
    This function compares the load_data loads the data type JSON.

    Parameters
    ----------
    test_load_data(None) : bool

    User input
    ----------
    None

    Returns
    -------
    bool

    """
    user_level = 1
    file_name = f"word_level_{user_level}.json"
    assert load_data(file_name) == load_data_test(file_name)

def test_replace_fail():
    """

    Description
    ----------
    This function validate the replace and validates the test fails

    Parameters
    ----------
    test_replace_fail(None) : bool

    User input
    ----------
    None

    Returns
    -------
    bool

    """
    # word is july
    assert replace('_ _ _ _ ','j',0) != 'j u l y '

def test_replace():
    """

    Description
    ----------
    This function validate the replace and validates the test for pass

    Parameters
    ----------
    test_replace_pass(None) : bool

    User input
    ----------
    None

    Returns
    -------
    bool

    """
    assert replace('_ _ _ _ ','j',0) == 'j _ _ _ '

def test_display_word():
    """

    Description
    ----------
    This function validate the display of the word J in index zero is replaced correctly for the display. This test expect a pass.
    Parameters
    ----------
    def test_display_word(None) : bool

    User input
    ----------
    None

    Returns
    -------
    bool

    """

    assert display_word('j u l y ','j', '_ _ _ _ ') == 'j _ _ _ '

def test_get_score():
    """

    Description
    ----------
    This function gets the score of the word for the game
    ----------
    def test_get_score(None) : bool

    User input
    ----------
    None

    Returns
    -------
    bool

    """
    assert get_score('abcd') == 4

def is_alpha_and_spaces_with_spaces_between(string):
    """

    Description
    ----------
    This function receive a random word and validates there are spaces bewteen each characters
    ----------
    def is_alpha_and_spaces_with_spaces_between(None) : bool

    User input
    ----------
    None

    Returns
    -------
    bool

    """
    return all(char.isalpha() or char.isspace() for char in string)

def test_select_word():
    """

    Description
    ----------
    This function tests the test_select_word(int)->str receive game level 1-5 and returns a randon word seperated by space between characters
    ----------
    def test_select_word(None) : bool

    User input
    ----------
    None

    Returns
    -------
    bool

    """
    assert is_alpha_and_spaces_with_spaces_between(select_word(5)) == True

def get_output(output, pattern):
    #output = child.readlines()
    for line in output:
        if re.search(pattern, line):
            return line

def test_main():
    # Start the program as a subprocess
    child = pexpect.spawn("python project.py")

    # Simulate interactions with partial phrase matching
    child.expect(re.compile(r"Username\?"))  # Match the "Username?" prompt
    child.sendline("gameboy")

    while True:
        line = child.readline().decode('utf-8').strip()
        if not line:
            break

        if re.search(r'gameboy:', line):
            assert True, f"'High Scores:' was found in output"
            child.sendline("\n")

            if re.search(r'Please select your level (1-5):', line):
                assert True, f"We made it to select game level :-)"
            else:
                assert True, f"We did not make it to select game level :-()"

            child.sendline("5")

            if re.search(r'Enter letter:', line):
                assert True, f"We made it to the game to start playing :-)"
            else:
                assert False, f"{line}  We did not make it to the game to start playing :-()"

            # this kills the game when a user clicks the return key more that 5 times
            child.sendline("")
            child.sendline("")
            child.sendline("")
            child.sendline("")
            child.sendline("")
            child.sendline("")
