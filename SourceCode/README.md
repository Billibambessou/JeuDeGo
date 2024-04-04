# Go game
A simple game of Go coded in python, with a Graphical User Interface (GUI)

## Technologies used
+ [Python 3.10.11](https://www.python.org/downloads/release/python-31011/)
+ [Tkinter Python Librairy](https://docs.python.org/3/library/tkinter.html)
+ [Time Python Librairy](https://docs.python.org/3/library/time.html)

## Requirement
The `.exe` file does not require anything to function
The code files require the version [3.10.10](https://www.python.org/downloads/release/python-31011/) as well as the Tkinter and Time librairies installed

## Usage
After downloading, open the `.exe` file. The launcher will appear, with this `README.md` file to provide explanation. You can select the size of the board, and start the game.

## Introduction to the Game of Go
The Go is an abstract strategy board game for two players, in which the aim is to surround more territory than the opponent. The game was invented in China more than 2,500 years ago and is believed to be the oldest board game continuously played to the present day.

### Game Rules
+ Game Board: Go is played on a grid of black lines (usually 19x19). Game pieces, called stones, are played on the intersections of the lines.
+ Starting the Game: The game begins with an empty board. Black makes the first move, after which White and Black alternate. White starts with a 6.5 points advantage to eliminate any tie possibility.
+ Playing the Game: A move consists of placing one stone of one's own color on an empty intersection on the board.
+ Capturing Stones: Stones are captured and removed from the board when they have no liberties left. A liberty is an adjacent node where there is no stone. Once the four liberties of a stone are taken by stones of the opposing color, it is captured. This is known as being 'atari'. Multiple adjacent stones of the same colors create a group, and every liberty of the group has to be taken in order to capture the whole group.
+ Forbidden Moves: A move that would recreate a previous board position is forbidden. This rule, called the 'ko rule', prevents unending repetition. It is also forbidden to play a stone that would instantly dying without modifying the current situation of the board.
+ Ending the Game: Players can skip their turn any time : if both players skip their turn, the game end.
+ Scoring: The player with the larger total of territory nodes and captured stones is the winner.

### Resources
For more detailed rules, strategies, and variations of the game, please refer to the following resources:
+ [Masters of Games](https://www.mastersofgames.com/rules/go-rules.htm)
+ [Wikipedia](https://en.wikipedia.org/wiki/Rules_of_Go)
+ [British Go Association](https://www.britgo.org/intro/intro2.html)

Enjoy the game!
