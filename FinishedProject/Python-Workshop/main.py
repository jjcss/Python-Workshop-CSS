# import turtle from Screen
from carManager import CarManager
# import player from Player
from turtle import Screen
from player import Player
# import car_manager from CarManager
from carManager import CarManager
# import scoreboard from Scoreboard
from scoreBoard import Scoreboard
# import time
import time

def main():
    #Screen set up
    screen = Screen()
    # Create a turtle player, a carManager & score variables to instantiate our objects
    screen.setup(width=600, height=600)
    screen.tracer(0)

    player = Player()
    manager = CarManager()
    board = Scoreboard()
    # Set up commands for the screen and the key the user will need to play game
    screen.listen()
    screen.onkey(player.moveUp, "Up")
    # Create a variable to use as Flag for the game logic

    """Game Logic"""
    gameOn = True
    # While loop
    while gameOn:
        # Delaying of the screen and update
        time.sleep(0.1)
        screen.update()
        # Create cars
        manager.createCar()
        # Move to cars to the right side of screen
        manager.moveForward()
        # Detect when the turtle player collides with a car and stop the game if this happens.
        # Uses a for-loop
        for car in manager.allCars:
            # Use the distance you'd like but the most accurate is 15-20.
            # If the distance of the car to "player" is less than 20.
            if car.distance(player) < 20:
                # Set flag to false
                gameOn = False
                # When turtle hits a car, GAME OVER.
                board.gameOver()
        # Detect when turtle player has reached the finish line.
        if player.successfulCross():
            # Return the turtle to starting
            player.resetPlayer()
            # Increase speed of cars.
            manager.increaseSpeed()
            # Every time the player crosses the level increases.
            board.increaseLevel()
    # Play again functionality
    playAgain = screen.textinput(title="Choose", prompt="Would you like to play again? Type 'y' for yes, or 'n' no")
    # If yes, clear screen and start game again.
    if playAgain == 'y':
        screen.clear()
        main()
    #Else, exit the screen on click
    else:
        screen.exitonclick()

main()