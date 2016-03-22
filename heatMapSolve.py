import json
import random
import copy
from gameBoardDraw import gameBoardDraw

gameBoardDrawVariable = gameBoardDraw(15)

pieceArray = []

'''
with open('pieces.txt', 'r+') as inFile:
    pieceArray = json.load(inFile)

gameBoard = [[0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0]]
'''


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


def getBoardValue(gameBoard):

    total = 0
    for row in gameBoard:
        for item in row:
            if item != 9:
                total = total + item

    return total


def flipPiece(piece):
    for row in piece:
        row = row.reverse()

    return piece

def rotateNinety(arrayToRotate):
    columns = len(arrayToRotate[0])
    rows = len(arrayToRotate)
    tempArray = [[0 for x in range(rows)] for x in range(columns)]
    for i in range(0, columns):
        for j in range(0, rows):
            tempArray[i][j] = arrayToRotate[j][columns-i-1]

    return tempArray

def addPieceAtLocation(gameBoard, piece, startX, startY):

    for i in range(0, len(piece)):
        for j in range(0, len(piece[i])):
            if piece[i][j] == 9:
                gameBoard[startY + i][startX + j] = 9

    return gameBoard

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



def insertPieceByCode(gameBoard, code):
    codeBits = code.split("|")

    piece = pieceArray[code[0]]

    pieceFlipped = int(codeBits[1])
    if pieceFlipped == 1:
        piece = flipPiece(piece)

    pieceRotations = int(codeBits[2])
    for x in range(pieceRotations):
        piece = rotateNinety(piece)

    pieceX = int(codeBits[3])
    pieceY = int(codeBits[4])

    # make sure that this is being passed by refernece, not by value
    gameBoard = addPieceAtLocation(gameBoard, piece, pieceX, pieceY)

    return gameBoard


def findOptimalSpot(gameBoard, piece, insertionCode):
    boardScore = -1
    insertionChar = insertionCode[0]
    insertionCode = "no insertion"
    for y in range (0, len(gameBoard)-1): # each row
        for x in range(0, len(gameBoard[0])-1): # each column
            for flipped in range(0,2):
                for rotations in range(0,4):
                    if isValidMove(gameBoard, piece, x, y):
                        tempGameBoard = copy.deepcopy(gameBoard)
                        tempGameBoard = addPieceAtLocation(tempGameBoard, piece, x ,y)
                        if getBoardValue(tempGameBoard) > boardScore:
                            boardScore = getBoardValue(tempGameBoard)
                            insertionCode = [insertionChar, flipped, rotations, x, y]
                    piece = rotateNinety(piece)
            piece = flipPiece(piece)

    return insertionCode




def populateTwentyThousandGames():
    for notGonnaUseThatB in range(1,101):

        with open('pieces.txt', 'r+') as inFile:
            pieceArray = json.load(inFile)

        gameBoard = [[0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0],
                     [0,0,0,0,0,0,0,0,0]]

        keepGoing = True
        pieceMoves = 0
        finalOutputStrings = []
        while keepGoing == True:
            pieceKeys = pieceArray.keys()
            indexOfPieceToRemove = int((random.random() * 100) % len(pieceArray))
            pieceToInsert = pieceArray[pieceKeys[indexOfPieceToRemove]]
            gameBoard = gameBoardHeatMap(gameBoard)
            insertionCode = [pieceKeys[indexOfPieceToRemove], 0, 0, 0, 0]
            moveArray = findOptimalSpot(gameBoard, pieceToInsert, insertionCode)
            if moveArray != "no insertion":
                moveArrayString = moveArray[0]+"|" + str(moveArray[1])+"|" + str(moveArray[2])+ "|" + str(moveArray[3]) + "|" + str(moveArray[4])
                finalOutputStrings.append(moveArrayString)
                gameBoard = insertPieceByCode(gameBoard, moveArrayString)
                gameBoard = gameBoardHeatMap(gameBoard)
                del pieceArray[pieceKeys[indexOfPieceToRemove]]
                pieceKeys.remove(pieceKeys[indexOfPieceToRemove])
            else:
                keepGoing = False
                finalOutputStrings.append(str(getBoardValue(gameBoard)))
                with open ("games/"+ str(notGonnaUseThatB)+".sqgm", "w") as writeFile:
                    for item in finalOutputStrings:
                        writeFile.write(item + "\n")

                if notGonnaUseThatB % 100 == 0:
                    print notGonnaUseThatB

        #gameBoardDrawVariable.drawGameBoard(gameBoard, 0)


with open('pieces.txt', 'r+') as inFile:
    pieceArray = json.load(inFile)

gameBoard = [[0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0],
             [0,0,0,0,0,0,0,0,0]]

with open("games/1.sqgm", "r+") as openFile:
    readString = openFile.readlines();

del readString[-1]
for line in readString:
    gameBoard = insertPieceByCode(gameBoard, line)
    gameBoard = gameBoardHeatMap(gameBoard)
    gameBoardDrawVariable = gameBoardDraw(15)
    gameBoardDrawVariable.drawGameBoard(gameBoard, 0)


'''

getBoardValue(gameBoard)
insertPieceByCode(gameBoard, "c|0|1|2|2")
getBoardValue(gameBoard)
'''


'''
Move string
piece letter name | flipped 1/0 | rotations 0-3 | X coordinate | Y coordinate
'''


