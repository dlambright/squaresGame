import json


pieceArray = []

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

    piece = pieceArray["c"]

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



gameBoard = gameBoardHeatMap(gameBoard)
insertPieceByCode(gameBoard, "c|0|1|2|2")




'''
Move string
piece letter name | flipped 1/0 | rotations 0-3 | X coordinate | Y coordinate
'''


