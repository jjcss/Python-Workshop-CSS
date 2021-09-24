# import turtle from Turtle
from turtle import Turtle
# Global variable for the font in the GUI
FONT = ("Courier", 24, "normal")

"""Class declaration"""
# class Scoreboard with super class Turtle
class Scoreboard(Turtle):
    # Defining the class
    """Score board class purpose is to indicate the level the player is currently on and control the game over sequence"""
        #Initialize with super class
    def __init__(self):
        super().__init__()
        # Color of the board on the screen
        self.color("black")
        # "Pen up" (the score doesn't move but just to be save)
        self.penup()
        # Hide turtle so you the score doesn't display a cursor
        self.hideturtle()
        # Initial level of the user
        self.levelNumb = 1
        # Display score
        self.displayScore()

    """Methods of the class"""
    # Display score method
    def displayScore(self):
        self.goto(-280, 260)
        self.write(arg=f"Level: {self.levelNumb}", move=False, align="left", font=FONT)

    # Increase the scoreboard method
    def increaseLevel(self):
        self.levelNumb += 1
        self.clear()
        self.displayScore()

    # Game over method
    def gameOver(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER!!", move=False, align="center", font=FONT)