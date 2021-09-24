# import turtle from Turtle
from hashlib import new
from math import remainder
from turtle import Turtle
# import random
import random

"""Global Variables"""
# List of colors (to pick at random)
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# Starting Moving distance of the cars on each refresh
startingDistance = 5
# Moving increment of the cars 
distanceIncrement = 5

"""Class declaration"""
# class CarManager 
class CarManager(Turtle):
    """Car manager class pupose is to generate all the random cars and move them across the screen """
    # Defining the class
    def __init__(self):

        # List of all cars
        self.allCars = []
        # Car speed which is the moving distances
        self.carSpeed = startingDistance

    """Methods of the class"""

    # Create car method
    def createCar(self):
        randomChance = random.randint(1, 6)
        if randomChance == 1:
            newCar = Turtle("square")
            newCar.shapesize(stretch_wid=1, stretch_len=2)
            newCar.penup()
            newCar.color(random.choice(COLORS))
            yRandom = random.randint(-250, 250)
            newCar.goto(300, yRandom)
            self.allCars.append(newCar)
    # Move method
    def moveForward(self):
        for car in self.allCars:
            car.backward(self.carSpeed)

    # Increase speed method
    def increaseSpeed(self):
        self.carSpeed += distanceIncrement