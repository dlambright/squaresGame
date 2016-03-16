# https://deepmind.com/alpha-go.html

from matplotlib import mpl, pyplot
from numpy import array
import random
import copy
import turtle
from Tkinter import *
from gameBoardDraw import gameBoardDraw


functionCalls = 0
comparisons = 0

gameBoardDrawVariable = gameBoardDraw(20)

def gameBoardHeatMap(gameBoard):
    for i in range(0,len(gameBoard)):
        for j in range(0, len(gameBoard[i])):
            if gameBoard[i][j] < 6:
                tempValue = 0
                if j < len(gameBoard[i])-1:         # Check Right
                    if gameBoard[i][j+1] < 6:
                        tempValue = tempValue + 1
                if i < len(gameBoard)-1:            # Check Down
                    if gameBoard[i+1][j] < 6:
                        tempValue = tempValue + 1
                if j > 0:                           # Check Left
                    if gameBoard[i][j-1] < 6:
                        tempValue = tempValue + 1
                if i > 0:                           # Check Up
                    if gameBoard[i-1][j] < 6:
                        tempValue = tempValue + 1

                gameBoard[i][j] = tempValue

    return gameBoard


def printBoard(gameBoard):
    for row in gameBoard:
        print row

def flipPiece(piece):
    for row in piece:
        row = row.reverse()

    return piece


def addPieceAtLocation(gameBoard, piece, startX, startY):
    
    for i in range(0, len(piece)):
        for j in range(0, len(piece[i])):
            if piece[i][j] == 9:
                gameBoard[startY + i][startX + j] = 9

    return gameBoard 

def isValidMove(gameBoard, piece, startX, startY):
    boardHeight = len(gameBoard)
    boardLength = len(gameBoard[0])
    pieceHeight = len(piece)
    pieceLength = len(piece[0])

    if startX + pieceLength > boardLength:
        #print "too long"
        return False
    if startY + pieceHeight > boardHeight:
        #print "too tall"
        return False

    for i in range(0, len(piece)):
        for j in range(0, len(piece[0])):
            if startX + j > len(gameBoard[0])-1 or startY + i > len(gameBoard)-1:
                return False

            if piece[i][j] == 9 and gameBoard[startY + i][startX + j] == 9:
                #print "overlap error"
                return False


    return True

    

def rotateNinety(arrayToRotate):
    columns = len(arrayToRotate[0])
    rows = len(arrayToRotate)
    tempArray = [[0 for x in range(rows)] for x in range(columns)]
    for i in range(0, columns):
        for j in range(0, rows):
            tempArray[i][j] = arrayToRotate[j][columns-i-1]

    return tempArray

def addPiece(gameBoard, piece):
    for y in range (0, len(gameBoard)-1): # each row
        for x in range(0, len(gameBoard[0])-1): # each column
            for ab in range(0,2):
                for ba in range(0,4):
                    if isValidMove(gameBoard, piece, x, y):
                        addPieceAtLocation(gameBoard, piece, x, y)
                        return gameBoard
                    else:
                        piece = rotateNinety(piece)
                piece = flipPiece(piece)
    return gameBoard

def gameBoardDeepCopy(gameBoard):

    tempGameBoard = [[0 for x in range(len(gameBoard))] for x in range(len(gameBoard[0]))]

    for i in range(0, len(gameBoard)):
        for j in range(0, len(gameBoard[i])):
            tempGameBoard[i][j] = gameBoard[i][j]

    return tempGameBoard

def gameBoardDeepCompare(gameBoard, gameBoardPrime):

    if gameBoard == None or gameBoardPrime == None:
        return True

    for i in range(0, len(gameBoard)):
        for j in range(0, len(gameBoard[i])):
            if gameBoard[i][j] != gameBoardPrime[i][j]:
                return False

    return True

def gameBoardIsFull(gameBoard):
    for row in gameBoard:
        for item in row:
            if item < 6:
                return False
    return True


def isOnWinningPath(gameBoard, pieceArray):
    #print "isOnWinningPath"
    if gameBoard == None:
        return False

    if len(pieceArray) == 0 or gameBoardIsFull(gameBoard):
        return True

    tempGameBoard = copy.deepcopy(gameBoard)

    pieceToInsert = pieceArray[0]
    pieceArray.pop(0)
    gameBoard = smartInsert(gameBoard, pieceToInsert, pieceArray)

    if gameBoardDeepCompare(gameBoard, tempGameBoard):
        return False

    return True

def smartInsert(gameBoard, piece, pieceArray):
    #print "smartInsert"
    count = 0
    for y in range (0, len(gameBoard)-1): # each row
        for x in range(0, len(gameBoard[0])-1): # each column
            for ab in range(0,2):
                for ba in range(0,4):
                    count = count + 1
                    #print count
                    if isValidMove(gameBoard, piece, x, y):
                        tempGameBoard = copy.deepcopy(gameBoard)
                        tempGameBoard = addPieceAtLocation(tempGameBoard, piece, x, y)
                        tempPieceArray = copy.deepcopy(pieceArray)

                        #check if there is a winning path from this spot
                        if isOnWinningPath(tempGameBoard, tempPieceArray):
                            addPieceAtLocation(gameBoard, piece, x, y)
                            return gameBoard

                    else:
                        piece = rotateNinety(piece)
                piece = flipPiece(piece)
    return None


def recursiveSolve(gameBoard, pieceArray):
    print len(pieceArray)
    if len(pieceArray) == 0:
        return gameBoard
    index = 0
    while (len(pieceArray) > 0):

        indexOfPieceToRemove = int((random.random() * 100) % len(pieceArray))

        pieceToTest = pieceArray[indexOfPieceToRemove]
        pieceArray.remove(pieceToTest)

        gameBoard = smartInsert(gameBoard, pieceToTest, pieceArray)
        gameBoard = gameBoardHeatMap(gameBoard)
        printBoard(gameBoard)
        gameBoardDrawVariable.drawGameBoard(gameBoard, index)
        index = index + 1

        print ""
    turtle.mainloop()
    turtle.done()




'''
# 5x5 board
pieceOne = [[0,9],[0,9],[0,9],[0,9],[0,9]]
pieceTwo = [[9,0],[9,9],[9,0]]
pieceThree = [[9,9],[9,0],[9,9]]
pieceFour = [[9,0],[9,0]]
pieceFive = [[9,0]]
pieceSix = [[0,9,9],[9,9,0]]
pieceSeven = [[0,9],[0,9],[9,9]]

pieceArray = [pieceOne, pieceTwo, pieceThree, pieceFour, pieceFive, pieceSix, pieceSeven]
'''
pieceOne = [[9,9],[9,9],[9,0]]
pieceTwo = [[9,0],[0,0]]
pieceSix = [[9,9],[9,0],[9,0]]
pieceThree = [[9,0],[9,0],[9,9],[0,9]]
pieceFour = [[9,0],[9,9]]
pieceFive = [[9,9]]

mainGameBoard = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

mainGameBoard = gameBoardHeatMap(mainGameBoard)

pieceArray = [pieceOne, pieceTwo, pieceThree, pieceFour, pieceFive, pieceSix]
recursiveSolve(mainGameBoard, pieceArray)
print "Comparisons : " + str(comparisons)

'''
print "Not Smart"

for piece in pieceArray:
    mainGameBoard = addPiece(mainGameBoard, piece)
    printBoard(mainGameBoard)
    print ""
'''












