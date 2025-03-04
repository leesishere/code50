
# user.py

## Modules

json
menu
os
time


## Functions

add_score(user_name, additional_score) -> None

### Description

This function receives a username and new points score as parameters.
The latest score is added to the JSON record in memory and stored in the user_scores.json file for future gameplay.

### Parameters

add_score(str, int) : None

### User input

None

### Return

None

---

## Function
bold(text) -> str
### Description

Receives a string and wraps ANSI escape code to create the effect of bolding the string when printed.

### Parameters

bold(str) : str

### User input

None

### Return

String with ANSI escape code before and after the original string to create bold text when printed.

---
## Function
file_exists(file_path) -> bool
### Description

This function determines if a file exists or not. If the file exists, it will return True and otherwise will return False.

### Parameters

file_exists(str) : bool

### User input

None

### Return

True if the file exists
False if the file does not exist

---

## Function
get_user_score(user_name) -> int
### Description

This function receives a username and returns username's total score.

### Parameters

get_user_score(str) : int

### User input

None

### Return

None

---

## Function
high_score(typer=True) -> None
### Description

The parameter default is True to print in typewriter mode on the screen.
This function clears the screen, retrieves all the username scores from the stored JSON, user_scores.json, and prints the high score in a table format in order from the highest to the lowest username scores.

### Parameters

high_score(bool) : None

### User input

Any key. Any key is a unique magical key that will allow the player to continue in the game.
If you cannot find the any key please refere to this website for more information to locate the any key on your qwerty key borad: https://en.wikipedia.org/wiki/Any_key

### Return

None

---

## Function
is_one_word(input_string) -> bool
### Description

Receives username as a parameter to validate the username is only one word.
If the username is one word, this function will return True; otherwise, it will return False.

### Parameters

is_one_word(str) : bool

### User input

None

### Return

True if the username is one work
False if the username is more than one word

---

## Function
load_data(file_name) -> json
### Description

Receives a parameter as a JSON file name and returns the file data in JSON format.

### Parameters

load_data(str) : json

### User input

None

### Return

File as JSON format or None if file does not exists

---

## Function
save_data(file_name, data) -> None
### Description

Receives JSON filename and new records to be added to the JSON data file.

### Parameters

save_data(str, str) : None

### User input

None

### Return

None

---

## Function
set_user() -> str
### Description

Clears the screen and requests the player's username as input. Calls is_one_word(username) to verify that the user name is one word.
Calls the verify_and_add_user(username) function to verify that the username exists in the user_scores.json file.
If not, it adds a user record to the user_scores.json to keep track of the usernames (player) and scores.

### Parameters

set_user(None) : str

### User input

User name

### Return

Username (player)

---

## Function
verify_and_add_user(user_name) -> None
### Description

Retrieves stored JSON data for the username (player). If the username does not exist in the JSON file, the function adds it to the stored JSON file, user_scores.json

### Parameters

verify_and_add_user(str) : None

### User input

None

### Return

None


### Data
file_name = 'data/user_scores.json'
