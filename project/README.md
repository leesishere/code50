# The Guessing Word Game
#### Video Demo:  <URL HERE>
#
#### **Description**
The Guessing Word Game aims for the player to guess the word within the lowest number of rounds possible.

#### **Game Background**

**Single player game** and the player is asked for their usernames. If this is the players first time playing, the game will create a username to keep track of each players score.

**There are five different levels:**
- 1  Easier Than Easy
    - Words with one syllable with a letter count less than 5.
- 2  Easy
    - Words with one syllable with a letter count between  5 and 7.
- 3  Normal
    - Words with two syllables with a letter count between 8 and 11.
- 4  Hard
    - Words with three or four syllables with a letter count between 12 and 15.
- 5  Difficult
    - Words with more than four syllables with a letter count more than 15.

## Sample Output:
\
Please select the game level 1-5

    ------------------------------
    1  Easier Than Easy
    2  Easy
    3  Normal
    4  Hard
    5  Difficult
    ------------------------------
    Please select your level (1-5): 4

#
The word list was retrieved from github [first20hours/google-10000-english](https://github.com/first20hours/google-10000-english). The word file used for this game: [google-10000-english-no-swears.txt](https://raw.githubusercontent.com/first20hours/google-10000-english/refs/heads/master/google-10000-english-no-swears.txt)

#### **Easter eggs**
- Instead of selecting 1-5 levels from the menu, enter qq and enter to quit the game.
    - A random farewell message will be displayed, and player will be asked if player want to hear a joke before player leave the game. It makes an api call to a free programmer [joke server](https://official-joke-api.appspot.com/jokes/programming/random), no joke.
- At any time, clicking the enter key six times or entering qq will end the game.
- While playing the game, player can enter a whole word when asked to enter a letter. If player guesses the correct word, player will get a higher score with zero rounds count on the first try, and if incorrect, this will only cost the player 1 round of play.
- A litter cheater: If player enters the same number of letters as the word, the game will search to see how many letters match in the word and only count this turn as a round. Be careful if player enters more than the number of letters of the word, this will give player a cheater alarm and add to player overall rounds the number of letters entered without searching for any matches in the word:-(
- The cheater! If player enters qwerty to guess the word, player wins every time:-)
---
# **Python Code files**
- [project.py](project.md)
- [menu.py](menu.md)
- [user.py](user.md)
- [test_project.py](test_project.md)

