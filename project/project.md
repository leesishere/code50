# project.py

## Modules
json
os
random
sys
time
user
---
## Function

### display_word(word, guess='', display='') -> str

Description

This function receives the word, guessed letter, and current display and loops through each letter of the word to determine if the guessed letter is in the word.
If the guessed letter is in the word, this function will call the replace function to replace the _ in the display variable with the guessed letter.

Parameters

display_word(str, str,str)->str

User input

None

Returns
str
---
## Function
### get_score(s, guess_count=0) -> int

Description

This function retrieves the word used in the game and the number of times the player took to guess it. Unique letters in the word are total and will be used to calculate the game score.
With zero guesses or tries, the score will be the number of unique letters in the word
10 or fewer guesses or tries, the score is 12 times the unique letters in the word
15 or fewer guesses or tries, the score is 7 times the unique letters in the word
20 or fewer guesses or tries, the score is 2 times the unique letters in the word
More than 20 tries, the player receives a zero score:-(

Parameters

get_score(str,int) : int

User input

None

Returns
-------
int as the score

## Function
### guess_menu(user_level, user_name) -> None

Description

Creates the game display to play the game. Retrieves a random word from the level JSON file and shows the current username's (player) score.
The display will show the number of letters for the word as underscores (_).
For example, if the word is July, the gameplay screen will show _ _ _ _, and with a guess of j, the screen will show j _ _ _ and so on.

Parameters

guess_menu(int,str) : int

User input

str as letter guessed or (y/n) to continue or not to continue gameplay.

Returns
-------
none

## Function
### load_data(file_name)

Description

This function is a generic JSON file retriever. It validates that the JSON file exists, loads it into memory, and returns the data set in JSON file format.

Parameters

load_data(str) : json

User input

None

Returns
-------
json

## Function
### main() -> None

Description

Retrieves username (player).
If this is the player's first time playing the game, their username will be added to the user_scores.json file to keep track of their scores.
The username (players) high scoreboard will be displayed on the screen.
The level menu will be displayed to the player to select which level they would like to play the game in
The game will start with selecting a random work to guess from either level 1-5 game level

Parameters

main(None) : None

User input

Any key to continue

Returns
-------
None

## Function
### replace(s, replacement, index) -> str

Description

This function replaces the correct guessed letter of the underscores (_) location.
For example, if the word is July and the current display is '_ _ _ _', this function will take in the display, '_ _ _ _'', replace the letter, such as j, the index location of j is in the word and return 'j _ _ _ '.

Parameters

replace(str,str,int) : str

User input

None

Returns
-------
str

## Function
### select_word(user_level) -> str

Description

This function receives the game level, loads the word JSON file with the appropriate level, and selects and returns a word at random to be played in the game.

Parameters

select_word(str) : str

User input

None

Returns
-------
str

### Data
error_count = 0


