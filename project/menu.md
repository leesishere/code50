# menu.py

## Modules
os
random
requests
sys


## Functions

### fairwell() -> str
Description
----------
This function takes no params and returns a fairwell phrase at random.

Parameters
----------
fairwell(None) : str
No parameters

User input
----------
None

Returns
-------
fairwell phrase as string
## Function
### get_joke() -> str
Description
----------
This function takes no params, performs api to https://official-joke-api.appspot.com/jokes/programming/random and returns a programming joke as string

Parameters
----------
get_joke(None): str
No parameters

User input
----------
None

Returns
-------
returns a programming joke as string
## Function
### i_quite() -> None
Description
----------
This function takes no params, calls fairwell() with an option to call get_joke() before exiting the program.

Parameters
----------
i_quite(None) : None
No parameters

User input
----------
How about a joke before you go (y/n)

Returns
-------
None
## Function
### is_no() -> bool
Description
----------
This function takes no params and validate user input entered y or n and exit program after 5 or more failed attempts.

Parameters
----------
i_quite(None) : True/False
No parameters

User input
----------
How about a joke before you go (y/n)

Returns
-------
True for n
False for y
## Function
### main_menu() -> str
Description
----------
Displays the game levels from 1-5 and retrieves from the user their selection of difficulty in the game levels and returns the level selected.
If the player enters qq, the game will print a farewell and ask the player if they would like to hear a programmer's joke before they exit the game.
The game will end if the player clicks any key besides 1-5 more than 5 times.

Parameters
----------
main_menu(None) : str
No parameters

User input
----------
User Level
Enter key more than 5 will call fairwell()
qq to exit game

Returns
-------
User level 1-5 or exists game
## Function
### menu_level(typer=True) -> None
Description
----------
This function takes True/False to determine whether the user-level menu is displayed on the screen in typewriter mode.

Parameters
----------
menu_level(bool): None

User input
----------
Select leve 1-5

Returns
-------
None
## Function
### processing() -> str

Description
----------
This function takes no params and prints a progress chart.

Parameters
----------
processing(None) : str
No parameters

User input
----------
None

Returns
-------
prints a progress chart:
[*                   ] 5%
[***                 ] 15%
[*****               ] 25%
[******              ] 30%
[********            ] 40%
[**********          ] 50%
[************        ] 60%
[**************      ] 70%
[****************    ] 80%
[******************* ] 95%
[********************] 100%
sleep(...)
sleep(seconds)

Delay execution for a given number of seconds.  The argument may be
a floating-point number for subsecond precision.
## Function
### type_writer(line) -> None

Description
----------
This function takes string and memics a typewriter mode

Parameters
----------
type_writer(str): None

User input
----------
None

Returns
-------
None

### Data
error_count = 0
