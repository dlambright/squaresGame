import turtle
from Tkinter import *

class gameBoardDraw(object):

    @staticmethod
    def drawGameBoard(self, gameBoard, step):
        wn=turtle.Screen()
        wn.bgcolor("black")
        wn.title("This is my screen title!")

        myturtle = turtle.Turtle()
        showColorizedBoard(myturtle, gameBoard)

        ts = turtle.getscreen()

        ts.getcanvas().postscript(file="duck" + str(step) + ".eps")


    @staticmethod
    def draw_empty_square(this_turtle, size, fillNumber):
        """Draw a square by drawing a line and turning through 90 degrees 4 times"""
        this_turtle.pendown()
        this_turtle.fill(False)
        for _ in range(4):
            this_turtle.forward(size)
            this_turtle.left(90)
        #this_turtle.fill(False)
        this_turtle.penup()

    @staticmethod
    def draw_filled_square(this_turtle, size, fillNumber):
        """Draw a square by drawing a line and turning through 90 degrees 4 times"""
        this_turtle.pendown()
        this_turtle.fill(True)
        for _ in range(4):
            this_turtle.forward(size)
            this_turtle.left(90)
        this_turtle.fill(False)
        this_turtle.penup()

    @staticmethod
    def showColorizedBoard(myturtle, gameBoard):
        myturtle.speed(0)
        square_size = 90

        for i in range(len(gameBoard)):
            myturtle.goto(-200, -square_size * i)
            for j in range(len(gameBoard[i])):
                if gameBoard[i][j] == 9:
                    myturtle.color("white")
                if gameBoard[i][j] == 1:
                    myturtle.color("red")
                if gameBoard[i][j] == 2:
                    myturtle.color("orange")
                if gameBoard[i][j] == 3:
                    myturtle.color("yellow")
                if gameBoard[i][j] == 4:
                    myturtle.color("green")

                draw_filled_square(myturtle, square_size, gameBoard[i][j])
                myturtle.fd(square_size)

    @staticmethod
    def addGrid(myturtle, gameBoard):
        myturtle.speed(0)
        square_size = 90

        for i in range(len(gameBoard)):
            myturtle.goto(-200, -square_size * i)
            for j in range(len(gameBoard[i])):
                draw_empty_square(myturtle, square_size, gameBoard[i][j])
                myturtle.fd(square_size)