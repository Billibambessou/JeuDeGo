from tkinter import *
from tkinter import scrolledtext
import main

def onBoardSizeChange():
    global BoardSize
    BoardSize = var.get()

def OnPlay():
    main.Draw_Window(BoardSize)
    LobbyWindow.destroy()
    main.MainLoop()

LobbyWindow = Tk()
xSize = 50
Window_width = 16*xSize
Window_height = 9*xSize
LobbyWindow.geometry(f"{Window_width}x{Window_height}")

PlayCanvas = Canvas(LobbyWindow, bg="lightBlue", border = -2)
PlayButton = Button(PlayCanvas, text="Play" , command=OnPlay, bg="lightBlue").pack(pady=10)
var = IntVar()
BoardSizeSelectorList = []
BoardSizeSelectorList.append(Radiobutton(PlayCanvas, text="19x19", variable=var, value=19, command=onBoardSizeChange, bg="lightBlue"))
BoardSizeSelectorList.append(Radiobutton(PlayCanvas, text="15x15", variable=var, value=15, command=onBoardSizeChange, bg="lightBlue"))
BoardSizeSelectorList.append(Radiobutton(PlayCanvas, text="13x13", variable=var, value=13, command=onBoardSizeChange, bg="lightBlue"))
BoardSizeSelectorList.append(Radiobutton(PlayCanvas, text="9x9", variable=var, value=9, command=onBoardSizeChange, bg="lightBlue"))

for i in range(len(BoardSizeSelectorList)):
    BoardSizeSelectorList[i].pack(side="bottom")
BoardSize = 13
BoardSizeSelectorList[2].select()
PlayCanvas.pack(side="left", fill="y")

READMEtext = scrolledtext.ScrolledText(LobbyWindow)
READMEtext.pack(side="left", fill="both")
READMEtext.insert(INSERT,f"{open('README.md', 'r').read()}")
READMEtext.configure(state ='disabled')

LobbyWindow.mainloop()
