# import turtle from Turtle
from turtle import Turtle

"""Global Variables"""
# Starting position
startingPosition = (0, -280)
# Moving (how much the turtle moves each time)
movingDistance = 10
#Finish Line Y-axis position
finishLineY = 280

"""Class declaration"""
# class Player with a super class Turtle
class Player(Turtle):
    # Defining the class
    """Player class purpose is to manage the turtle we're controlling to cross the road"""
        # Initialize with super class
    def __init__(self):
        super().__init__()
        # Shape of the turle
        self.shape("turtle")
        # Color of turtle?
        self.color("green")
        # "Pen" up (prevents the "turtle" from drawing a line after moving)
        self.penup()
        # Reset player method
        self.resetPlayer()
        # Set the heading of the "turtle"
        self.setheading(90)

    """Methods of the class"""   
    # Move up method
    def moveUp(self):
        self.forward(movingDistance)
    # Method to reset to starting position
    def resetPlayer(self):
        self.goto(startingPosition)

    # Method for what happens when player gets to finish line
    def successfulCross(self):
        if self.ycor() > finishLineY:
            return True
        else:
            return False