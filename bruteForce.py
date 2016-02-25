from matplotlib import mpl, pyplot
import numpy as np
import random
import copy

functionCalls = 0
comparisons = 0


def showColorizedBoard(gameBoard):
    # make a color map of fixed colors
    cmap = mpl.colors.ListedColormap(['black','red'])
    bounds=[-1,0,2]
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

    # tell imshow about color map so that only set colors are used
    img = pyplot.imshow(gameBoard,
                        interpolation='nearest',
                        cmap = cmap,
                        norm=norm)

    # make a color bar
    #pyplot.colorbar(img,cmap=cmap,
    #                norm=norm,boundaries=bounds,ticks=[-5,0,5])

    pyplot.show()

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
            if piece[i][j] == 1:
                gameBoard[startY + i][startX + j] = 1

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

            if piece[i][j] == 1 and gameBoard[startY + i][startX + j] == 1:
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
    for i in range(0, len(gameBoard)):
        for j in range(0, len(gameBoard[i])):
            if gameBoard[i][j] != gameBoardPrime[i][j]:
                return False

    return True

def gameBoardIsFull(gameBoard):
    for row in gameBoard:
        for item in row:
            if item == 0:
                return False
    return True


def isOnWinningPath(gameBoard, pieceArray):

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
    for y in range (0, len(gameBoard)-1): # each row
        for x in range(0, len(gameBoard[0])-1): # each column
            for ab in range(0,2):
                for ba in range(0,4):
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
    return gameBoard


def recursiveSolve(gameBoard, pieceArray):
    if len(pieceArray) == 0:
        return gameBoard

    while (len(pieceArray) > 0):

        indexOfPieceToRemove = int((random.random() * 100) % len(pieceArray))

        pieceToTest = pieceArray[indexOfPieceToRemove]
        pieceArray.remove(pieceToTest)

        gameBoard = smartInsert(gameBoard, pieceToTest, pieceArray)
        #printBoard(gameBoard)
        showColorizedBoard(gameBoard)
        print ""






pieceOne = [[0,1],[1,1],[0,1]]
pieceTwo = [[1,1],[1,0],[1,1]]
pieceThree = [[1,0],[1,0],[1,0],[1,0]]
pieceFour = [[1,0],[1,0],[1,0]]

#pieceFour = [[1,0]]
#pieceFive = [[1,0],[1,0]]
#pieceSix = [[1,0],[1,1],[0,1]]
#pieceSeven = [[0,1],[0,1],[1,1]]
#pieceThree = [[1,1],[1,0]]
#pieceFour = [[1,0],[1,0]]

pieceArray = [pieceOne, pieceTwo, pieceThree, pieceFour] #, pieceFive, pieceSix, pieceSeven]

roomToMove = True

mainGameBoard = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

recursiveSolve(mainGameBoard, pieceArray)
print "Comparisons : " + str(comparisons)

'''
print "Not Smart"

for piece in pieceArray:
    mainGameBoard = addPiece(mainGameBoard, piece)
    printBoard(mainGameBoard)
    print ""
'''












