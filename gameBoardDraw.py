import turtle
import datetime
from Tkinter import *

class gameBoardDraw(object):

    def __init__(self, square_size):
        self.turtle = turtle.Turtle
        self.squareSize = square_size
        self.moveNumber = 0
        self.startX = 0
        self.startY = 300 # set hieght / 2

    def draw_empty_square(self):
        """Draw a square by drawing a line and turning through 90 degrees 4 times"""
        self.turtle.pendown()
        self.turtle.fill(False)
        for _ in range(4):
            self.turtle.forward(self.squareSize)
            self.turtle.left(90)
        #this_turtle.fill(False)
        self.turtle.penup()

    def draw_filled_square(self):
        """Draw a square by drawing a line and turning through 90 degrees 4 times"""
        self.turtle.pendown()
        self.turtle.fill(True)
        for _ in range(4):
            self.turtle.forward(self.squareSize)
            self.turtle.left(90)
        self.turtle.fill(False)
        self.turtle.penup()

    def addGrid(self, gameBoard):
        self.turtle.speed(0)
        self.turtle.color("black")

        for i in range(len(gameBoard)):
            self.turtle.goto(self.startX, self.startY-(i*self.squareSize))
            for j in range(len(gameBoard[i])):
                self.draw_empty_square()
                self.turtle.fd(self.squareSize)
        self.turtle.hideturtle()


    def showColorizedBoard(self, gameBoard):
        self.turtle.speed(0)

        for i in range(len(gameBoard)):
            self.turtle.penup()
            self.turtle.goto(self.startX, self.startY-(i*self.squareSize))
            self.turtle.pendown()
            for j in range(len(gameBoard[i])):
                if gameBoard[i][j] == 9:
                    self.turtle.color("white")
                if gameBoard[i][j] == 1:
                    self.turtle.color("red")
                if gameBoard[i][j] == 2:
                    self.turtle.color("orange")
                if gameBoard[i][j] == 3:
                    self.turtle.color("yellow")
                if gameBoard[i][j] == 4:
                    self.turtle.color("green")

                self.draw_filled_square()  #gameBoard[i][j])
                self.turtle.fd(self.squareSize)


        self.addGrid(gameBoard)

        self.turtle.penup()
        self.startY = int(self.turtle.position()[1] - (2 * self.squareSize))



    def drawGameBoard(self, gameBoard, step):
        wn = turtle.Screen()
        wn.bgcolor("gray")
        wn.title("Shut up Drew Brees")
        wn.setup( width = 300, height = 1000, startx = None, starty = None)
        self.moveNumber = step

        self.turtle = turtle.Turtle()
        self.showColorizedBoard(gameBoard)#self.turtle.position[0], (self.turtle.position[1] + (len(gameBoard) + 2) * self.squareSize))

        ts = self.turtle.getscreen()

        ts.getcanvas().postscript(file="game_" + str(datetime.datetime.now()) + ".eps")# + str(step) + ".eps")

