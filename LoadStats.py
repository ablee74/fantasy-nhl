#Loads stats for each player. Taken from excel database
#to player class objects
import openpyxl
from Player import *
wb = openpyxl.load_workbook('Player Database.xlsx')


def getPlayer(name, season):
    """This will pull player info from excel Database and put it in the
    player object - Player.py"""
    global wb
    ws = wb.get_sheet_by_name(season)
    notFound = True
    r = 5       #Names start at row 5
    while notFound and ws.cell(row = r, column = 1).value != None:
        if ws.cell(row = r, column = 1).value == name:
            notFound = False
        else:
            r = r + 1

    c = 2
    notFound = True
    while notFound and ws.cell(row = 4, column = c).value != None:
        if ws.cell(row = 4, column = c).value == "Team":
            notFound = False
        else:
            c = c + 1

    p = Player(name, ws.cell(row = r, column = c).value)

##    c = 2
##    notFound = True
##    while notFound and ws.cell(row = 4, column = c).value != None:
##        if ws.cell(row = 4, column = c).value == "G":
##            notFound = False
##        else:
##            c = c + 1

    traitL = ["G","Assists","Shots on Goal","TOI"]
    toAdd = []
    for trait in traitL:
        c = 2
        notFound = True
        while notFound and ws.cell(row = 4, column = c).value != None:
            if ws.cell(row = 4, column = c).value == trait:
                notFound = False
                toAdd.append(ws.cell(row = r, column = c).value)
            else:
                c = c + 1
    
    p.goals = int(toAdd[0])
    p.assists = int(toAdd[1])
    p.SOG = int(toAdd[2])
    y = noComma(toAdd[3])
    p.TOI = int(y)

    return p # end line

def noComma(x):
    """x is a string that represents a number, it has commas every 3
    digits"""
    if len(x)>3:
        y = x[:-4] + x[-3:]
    else:
        y = x

    return y

        
    


