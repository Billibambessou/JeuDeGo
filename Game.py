import tkinter
from tkinter import *
from time import sleep

def print_Goban():
    print("<--------------------------------------------------------->")
    for i in range(nb):
        print(goban[i])
    print("<--------------------------------------------------------->")

def Double_In(list, item):
    for i in range(len(list)):
        if item in list[i]:
            return i
    return False

def Concatenate_Group_Lists2():
    setToFalse = True
    i = 0
    while setToFalse:
        if i == 0:
            pass
        ConcatenateBool = False
        ToConcatenate = []
        for j in range(len(list_of_groups[i])):
            itemLiberties = Find_Liberties(list_of_groups[i][j][0], list_of_groups[i][j][1])
            ConcatenateBool = False
            for k in range(len(itemLiberties)):
                    if ConcatenateBool != True:
                        isLibertieInAnotherGroup = Double_In(list_of_groups[i+1:], itemLiberties[k])

                        if type(isLibertieInAnotherGroup) == int:
                            if gameZoneCanvas.itemcget(goban[list_of_groups[i][0][1]][list_of_groups[i][0][0]],"fill") == gameZoneCanvas.itemcget(goban[list_of_groups[isLibertieInAnotherGroup+i+1][0][1]][list_of_groups[isLibertieInAnotherGroup+i+1][0][0]], "fill"):
                                    ConcatenateBool = True
                                    if type(Double_In(ToConcatenate, itemLiberties[k])) == bool:
                                        ToConcatenate.append((isLibertieInAnotherGroup+i+1, itemLiberties[k]))

        for j2 in range(len(ToConcatenate)):
            list_of_groups[i] = list_of_groups[i] + list_of_groups[ToConcatenate[j2][0]]
        if len(ToConcatenate) > 0:
            for j2 in range(len(ToConcatenate)):
                list_of_groups.pop(ToConcatenate[j2][0] - j2)
        i += 1
        if i == len(list_of_groups):
            setToFalse = False

def SupprimerGroupe(GroupIndex):
    #print(GroupIndex)
    if gameZoneCanvas.itemcget(goban[list_of_groups[GroupIndex][0][1]][list_of_groups[GroupIndex][0][0]], "fill") == "white":
        JoueurNoirCaptured.config(text=f"{float(JoueurNoirCaptured.cget('text')) + len(list_of_groups[GroupIndex])}")
    else:
        JoueurBlancCaptured.config(text=f"{float(JoueurBlancCaptured.cget( 'text')) + len(list_of_groups[GroupIndex])}")
    for i in range(len(list_of_groups[GroupIndex])):
        gameZoneCanvas.delete(goban[list_of_groups[GroupIndex][i][1]][list_of_groups[GroupIndex][i][0]])
        goban[list_of_groups[GroupIndex][i][1]][list_of_groups[GroupIndex][i][0]] = 0
    list_of_groups.pop(GroupIndex)

def Sum_Of_a_Group_Liberties(GroupIndex):
    totalLiberties = 0
    for i in range(len(list_of_groups[GroupIndex])):
        totalLiberties += len(Get_rid_of_Dead_Liberties(Find_Liberties(list_of_groups[GroupIndex][i][0], list_of_groups[GroupIndex][i][1])))

    return totalLiberties

def Board_Check():
    for i in range(len(goban)):
        for j in range(len(goban[i])):
            if goban[i][j] != 0:
                IsStoneInList = Double_In(list_of_groups, (j,i))
                if not IsStoneInList:
                    list_of_groups.append([(j,i)])
    for i in range(4):
        Concatenate_Group_Lists2()
    list_of_groupsLiberties.clear()
    for i in range(1, len(list_of_groups)):
        list_of_groupsLiberties.append(Sum_Of_a_Group_Liberties(i))
    for i in range(len(list_of_groupsLiberties)):
        if list_of_groupsLiberties[i] == 0 and not LastStonePlaced in list_of_groups[i]:
            print(i, list_of_groups[i])
            if len(list_of_groups)>= i+1:
                SupprimerGroupe(i+1)

def Get_rid_of_Dead_Liberties(tempLiberties):
    #vérifier si une libertée est prise.
    tempList = []
    for i in range(len(tempLiberties)):
        if goban[tempLiberties[i][1]][tempLiberties[i][0]] != 0:
            tempList.append(i)
    for i in range(len(tempList)):
        tempLiberties.pop(tempList[i]-i)
    return tempLiberties

def Find_Liberties(x,y):
    #récuperer la liste de toutes les libertées
    liberties = []
    if x == 0:
        liberties.append((x+1, y))
    elif x == nb-1:
        liberties.append((x-1, y))
    else:
        liberties.append((x-1, y))
        liberties.append((x+1, y))
    if y == 0:
        liberties.append((x, y+1))
    elif y == nb-1:
        liberties.append((x, y-1))
    else:
        liberties.append((x, y-1))
        liberties.append((x, y+1))
    return liberties

def Changement_de_joueur():
    global joueur
    if joueur == "black":
        joueur="white"
        HuDCanvas.itemconfig(JoueurBlancVisual, width=5)
        HuDCanvas.itemconfig(JoueurNoirVisual, width=0)
    else:
        joueur = "black"
        HuDCanvas.itemconfig(JoueurBlancVisual, width=0)
        HuDCanvas.itemconfig(JoueurNoirVisual, width=5)

def Place_Stone_on_given_point(x,y, Xindex, Yindex):
    global LastStonePlaced
    size = BoardSize/(2*(nb+1))
    goban[Yindex][Xindex] = gameZoneCanvas.create_oval(x-size, y-size, x+size, y+size, fill=joueur)
    LastStonePlaced = (Xindex, Yindex)

def Find_Coordinate_on_click(clickX, clickY):
    pointX = coordonees[0][0]
    for i in range(1,len(coordonees[0])):
        diff1 = abs(clickX-pointX)
        diff2 = abs(clickX-coordonees[0][i])
        if diff1 > diff2:
            pointX = coordonees[0][i]
    pointY = coordonees[1][0]
    for i in range(1,len(coordonees[1])):
        diff1 = abs(clickY-pointY)
        diff2 = abs(clickY-coordonees[1][i])
        if diff1 > diff2:
            pointY = coordonees[1][i]
    return pointX, pointY

def Skip_Turn():
    global skipedTurn
    if not skipedTurn:
        skipedTurn = True
        Changement_de_joueur()
    else:
        gameZoneCanvas.unbind("<Button-1>")
        gameZoneCanvas.unbind("<Motion>")
        gameZoneCanvas.delete(ThickLineV)
        gameZoneCanvas.delete(ThickLineH)
        EndGameText.place(x=HuDCanvasWidth * 0.5 - textFontSize * fontToPixelsRatio / 1.9, y=HuDCanvasHeight * 0.34)
        EndGameText.config(bg="#a84d11")

def OnCanvasClick(event):
    #trouve les coordonées du point le plus près de l'endroit cliqué
    pointX, pointY = Find_Coordinate_on_click(event.x, event.y)
    if goban[coordonees[1].index(pointY)][coordonees[0].index(pointX)] == 0:
        Place_Stone_on_given_point(pointX, pointY, coordonees[0].index(pointX), coordonees[1].index(pointY))
        Board_Check()
        print("liste des groupes :",list_of_groups)
        print("liste des libertées de chaque groupe :",list_of_groupsLiberties)
        Changement_de_joueur()
        print("----------------------FIN DU TOUR-------------------------------")
    else:
        Find_Liberties(coordonees[0].index(pointX), coordonees[1].index(pointY))
        print("IL Y A DEJA UNE PIERRE ICI CONNARD")

def motion(event):
    global ThickLineH, ThickLineV
    lineX, lineY = Find_Coordinate_on_click(event.x, event.y)
    if gameZoneCanvas.coords(ThickLineV)[0] != lineX:
        gameZoneCanvas.coords(ThickLineV,lineX, BoardSize / (nb + 1), lineX, (nb) * (BoardSize) / (nb + 1))
        gameZoneCanvas.itemconfig(ThickLineV, state="normal")
    if type(ThickLineH) == int and gameZoneCanvas.coords(ThickLineH)[1] != lineY:
        gameZoneCanvas.coords(ThickLineH, screen_width * 0.405 - BoardSize / 2 + (BoardSize) / (nb + 1), lineY, screen_width * 0.405 + BoardSize / 2 - (BoardSize) / (nb + 1), lineY)
        gameZoneCanvas.itemconfig(ThickLineH, state="normal")
def onHuDCanvasClick(event):
    print("click abscisse :",event.x, "click ordonnée :", event.y)

def on_Window_Resize(event):
    global Window_height, Window_width
    if Window_height != event.height or Window_width != event.width:
        print(f"window height : {event.height} --- old window height : {Window_height}")
        print(f"window width : {event.width} --- old window width : {Window_width}")
        print("--------------------------------------------------------------------")
        Window_height = event.height
        Window_width = event.width

def Draw_Window(InputNb):
    global mainWindow, screen_width, screen_height, GameTaskBar,gameZoneCanvas,HuDCanvas, JoueurBlancVisual, JoueurNoirVisual, CapturedStoneText, JoueurNoirCaptured, JoueurBlancCaptured, goban, coordonees, list_of_groups, list_of_groupsLiberties, joueur, nb, BoardSize, WhiteBonus, ThickLineH, ThickLineV, skipedTurn, EndGameText, HuDCanvasWidth, textFontSize, fontToPixelsRatio, HuDCanvasHeight

    #création de la fenetre
    mainWindow = Tk()
    mainWindow.attributes("-fullscreen", True)
    #mainWindow.attributes("-topmost", True)
    mainWindow.update()
    sleep(0.1)
    screen_width = mainWindow.winfo_width()
    screen_height = mainWindow.winfo_height()

    GameTaskBar = tkinter.Canvas(mainWindow, height=screen_height*0.05, width=screen_width, bg="blue", bd=-2)
    GameTaskBar.grid(column=0, row=0, columnspan=3, sticky="nswe")
    CloseButton = Button(GameTaskBar, width=f'{int(screen_height*0.003)}', bg="red", text="×", command=mainWindow.destroy).place(x=screen_width-screen_height*0.04, y=screen_height*0.01)

    #création du canvas de jeu
    gameZoneCanvas = tkinter.Canvas(mainWindow, height=screen_height*0.95, width=screen_width*0.81, bg="#E7C966", bd=-2)
    gameZoneCanvas.bind("<Button-1>", OnCanvasClick)
    gameZoneCanvas.bind('<Motion>', motion)
    ThickLineH = False
    ThickLineV = False
    gameZoneCanvas.grid(row=1, padx=0, pady=0, sticky="nswe")

    ThickLineV = gameZoneCanvas.create_line(0,0,0,0, width=2)
    gameZoneCanvas.itemconfig(ThickLineV, state="hidden")
    ThickLineH = gameZoneCanvas.create_line(0,0,0,0, width=2)
    gameZoneCanvas.itemconfig(ThickLineH, state="hidden")

    HuDCanvas = tkinter.Canvas(mainWindow, height=screen_height*0.95, width=screen_width*0.19, bg="#a84d11", bd=-2)
    HuDCanvas.grid(column=2, row=1, padx=0,pady=0, sticky="nswe")
    #HuDCanvas.bind("<Button-1>", onHuDCanvasClick)
    HuDCanvasWidth = int(HuDCanvas.cget('width'))
    HuDCanvasHeight = int(HuDCanvas.cget('height'))
    JoueurNoirVisual = HuDCanvas.create_oval(HuDCanvasWidth*0.2, HuDCanvasHeight*0.05, HuDCanvasWidth*0.4, HuDCanvasHeight*0.05 + HuDCanvasWidth*0.2, fill="black", outline="red", width=5)
    JoueurBlancVisual = HuDCanvas.create_oval(HuDCanvasWidth*0.8, HuDCanvasHeight*0.05, HuDCanvasWidth*0.6, HuDCanvasHeight*0.05 + HuDCanvasWidth*0.2, fill="white", outline="red", width=0)
    HuDCanvas.create_line(HuDCanvasWidth*0.2,HuDCanvasHeight*0.17, HuDCanvasWidth*0.8, HuDCanvasHeight*0.17) #ligne horizontale 1
    HuDCanvas.create_line(HuDCanvasWidth*0.2,HuDCanvasHeight*0.21, HuDCanvasWidth*0.8, HuDCanvasHeight*0.21) #ligne horizontale 2
    HuDCanvas.create_line(HuDCanvasWidth*0.2,HuDCanvasHeight*0.27, HuDCanvasWidth*0.8, HuDCanvasHeight*0.27) #ligne horizontale 3
    HuDCanvas.create_line(HuDCanvasWidth*0.2, HuDCanvasHeight*0.17, HuDCanvasWidth*0.2, HuDCanvasHeight*0.27) #ligne verticale 1
    HuDCanvas.create_line(HuDCanvasWidth*0.8, HuDCanvasHeight*0.17, HuDCanvasWidth*0.8, HuDCanvasHeight*0.27) #ligne verticale 2
    HuDCanvas.create_line(HuDCanvasWidth*0.5, HuDCanvasHeight*0.21, HuDCanvasWidth*0.5, HuDCanvasHeight*0.27) #ligne verticale 3

    textFontSize = int(HuDCanvasWidth*0.3/10)
    fontToPixelsRatio = 100/9
    CapturedStonesText = Label(HuDCanvas, text="Captured Stones", font=("Arial", textFontSize))
    CapturedStonesText.place(x=HuDCanvasWidth*0.5-textFontSize*fontToPixelsRatio/2,y=HuDCanvasHeight*0.18)
    CapturedStonesText.config(bg="#a84d11")
    JoueurNoirCaptured = Label(HuDCanvas, text="0", font=("Arial",int(textFontSize*1.2)))
    JoueurNoirCaptured.place(x=HuDCanvasWidth*0.35-textFontSize, y=HuDCanvasHeight*0.22)
    JoueurNoirCaptured.config(bg="#a84d11")
    WhiteBonus = 6.5
    JoueurBlancCaptured = Label(HuDCanvas, text=f"{WhiteBonus}", font=("Arial", int(textFontSize*1.2)))
    JoueurBlancCaptured.place(x=HuDCanvasWidth*0.65-textFontSize, y=HuDCanvasHeight*0.22)
    JoueurBlancCaptured.config(bg="#a84d11")

    ButtonPasser = Button(HuDCanvas, text="Skip turn", bg="#a84d11", command=Skip_Turn)
    ButtonPasser.place(x=HuDCanvasWidth*0.5-HuDCanvasWidth/146*15, y=HuDCanvasHeight*0.3)

    EndGameText = Label(HuDCanvas, text="The game has ended", font=("Arial", textFontSize))

    #création de la grille
    nb = InputNb #la taille du tableau nb x nb
    BoardSize = screen_height*0.95
    if BoardSize >= screen_width*0.81:
        BoardSize = screen_width*0.81
    for i in range(nb): #création des lines horizontales
        gameZoneCanvas.create_line(screen_width*0.405-BoardSize/2+(BoardSize)/(nb+1), (i+1)*(BoardSize)/(nb+1), screen_width*0.405-BoardSize/2+nb*(BoardSize)/(nb+1), (i+1)*(BoardSize)/(nb+1))
    for i in range(nb): #création des lines verticales
        gameZoneCanvas.create_line(screen_width*0.405-BoardSize/2+(i+1)*(BoardSize)/(nb+1), BoardSize-(nb)*(BoardSize)/(nb+1), screen_width*0.405-BoardSize/2+(i+1)*(BoardSize)/(nb+1), (nb)*(BoardSize)/(nb+1))

    #création de la grille de boutons
    goban = []
    for i in range(nb):
        tempList = [0 for j in range(nb)]
        goban.append(tempList)

    #enregistre les coordonées X et Y des points
    coordonees = []
    coordonees.append([screen_width*0.405-BoardSize/2+(i+1)*(BoardSize)/(nb+1) for i in range(nb)])
    coordonees.append([(i+1)*(BoardSize)/(nb+1) for i in range(nb)])

    list_of_groups = [[]]
    list_of_groupsLiberties = []

    joueur = "black"
    skipedTurn = False

#lancement de la fenetre
def MainLoop():
    while True:
        mainWindow.update()
        mainWindow.update_idletasks()