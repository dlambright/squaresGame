import os
import json

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


def getNextPiece():
    user_input = raw_input("here, m8:")
    piece = pieceArray[user_input]
    for row in piece:
        print row

    return piece


def getNextMove():
    print "Yeah, do this one, Duzn"


newPiece = getNextPiece()
