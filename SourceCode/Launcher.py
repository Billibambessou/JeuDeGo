from tkinter import *
from tkinter import scrolledtext
from time import sleep
import os, sys

import Game

def get_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, filename)
    else:
        return filename

def onBoardSizeChange():
    global BoardSize
    BoardSize = var.get()

def OnPlay():
    Game.Draw_Window(BoardSize)
    LobbyWindow.destroy()
    sleep(1)
    Game.MainLoop()

LobbyWindow = Tk()
LobbyWindow.title("Go Game")
LobbyWindow.iconphoto(False, PhotoImage(file = get_path("Icon.png")))
xSize = 45
Window_width = 16*xSize
Window_height = 9*xSize
LobbyWindow.geometry(f"{Window_width}x{Window_height}")

PlayCanvas = Canvas(LobbyWindow, bg="lightBlue", border = -2)
PlayButton = Button(PlayCanvas, text="Play" , command=OnPlay, bg="lightBlue").pack(pady=10)
var = IntVar()
BoardSizeSelectorList = []
BoardSizeSelectorList.append(Radiobutton(PlayCanvas, text="19x19", variable=var, value=19, command=onBoardSizeChange, bg="lightBlue"))
BoardSizeSelectorList.append(Radiobutton(PlayCanvas, text="13x13", variable=var, value=13, command=onBoardSizeChange, bg="lightBlue"))
BoardSizeSelectorList.append(Radiobutton(PlayCanvas, text="9x9", variable=var, value=9, command=onBoardSizeChange, bg="lightBlue"))

for i in range(len(BoardSizeSelectorList)):
    BoardSizeSelectorList[i].pack(side="bottom")
BoardSize = 13
BoardSizeSelectorList[2].select()
PlayCanvas.pack(side="left", fill="y")

READMEtext = scrolledtext.ScrolledText(LobbyWindow)
READMEtext.pack(side="left", fill="both")
READMEtext.insert(INSERT,"The Go is an abstract strategy board game for two players, in which the aim is\nto surround more territory than the opponent. The game was invented in China\nmore than 2,500 years ago and is believed to be the oldest board game\ncontinuously played to the present day.\n\n----------Game Rules-------------\n- Game Board: Go is played on a grid of black lines,\n(usually 19x19 but it is recommended to start on 9x9 or 13x13).\nGame pieces, called stones, are played on the intersections of the lines.\n- Starting the Game: The game begins with an empty board. Black makes the first move, after which White and Black alternate.\nWhite starts with a 6.5 points advantage to eliminate any tie possibility.\n- Playing the Game: A move consists of placing one stone of one's own color\non an empty intersection on the board.\n- Capturing Stones: Stones are captured and removed from the board when they\nhave no liberties left. A liberty is an adjacent node where there is no stone.\nOnce the four liberties of a stone are taken by stones of the opposing color, itis captured. This is known as being 'atari'.\nMultiple adjacent stones of the same colors create a group, and every liberty\nof the group has to be taken in order to capture the whole group.\n- Forbidden Moves: A move that would recreate a previous board position is\nforbidden. This rule, called the 'ko rule', prevents unending repetition.\nIt is also forbidden to play a stone that would instantly die without modifying\nthe current situation of the board.\n- Ending the Game: Players can skip their turn any time : if both players skip \ntheir turn, the game ends.\n- Scoring: The player with the larger total of territory nodes and captured\nstones is the winner.\n\n---------Resources-------------\nFor more detailed rules, strategies, and variations of the game, please refer tothe following resources:\n- https://www.mastersofgames.com/rules/go-rules.htm\n- https://en.wikipedia.org/wiki/Rules_of_Go\n- https://www.britgo.org/intro/intro2.html\n\nEnjoy the game!")
READMEtext.configure(state ='disabled')

LobbyWindow.mainloop()
