import pytest
from project import load_data, select_word, replace, replace, display_word, get_score, guess_menu, main
import os, json

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

def test_main(monkeypatch, capsys):

# def test_ main()
#    user_name = user.set_user()
#    user.high_score()
#    input()
#    user_level = main_menu()

#    def guess_menu(user_level, user_name)->None

    inputs = iter(["gameboy", "", "5", "", "", "", "", "", ""])  # First input for `user_name`, second for `input()`, third game level
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    # Running the main function
    main()

    # Capturing printed output
    captured = capsys.readouterr()

    assert "Username?" in output, "Prompt for username is missing."
    assert "High Scores:" in output, "High scores are not displayed."
    assert "1 - gene:       382" in output, "High score 1 is missing."
    assert "2 - jamey:      324" in output, "High score 2 is missing."
    assert "3 - gameboy:    252" in output, "High score 3 is missing."
    assert "Press any key to continue" in output, "Prompt to continue is missing."
    assert "\033[H\033[J" in output_lines, "Clear screen sequence not found in printed output."
    assert "Please select the game level 1-5" in output, "Game level selection prompt is missing."
    assert "1  Easier Than Easy" in output, "Game level options are missing."
    assert "5  Difficult" in output, "Game level options are incomplete."
    assert "Playing level 5   Total score: 252" in output, "Level confirmation and score are missing."
    assert "Word guess game: _ _ _ _ _ _ _ _ _ _ _ _" in output, "Game display is missing."
