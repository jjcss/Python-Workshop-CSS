# from turtle import Turtle, Screen

# timmy = Turtle()
# screen = Screen()

# timmy.forward(20)
# timmy.right(90)
# timmy.forward(50)
# timmy.left(30)
# timmy.forward(50)

# timmy.begin_fill()
# while True:
#     timmy.speed(10)
#     timmy.color('red', 'yellow')
#     timmy.forward(200)
#     timmy.left(170)
#     if abs(timmy.pos()) < 1:
#         break

# timmy.end_fill()
# screen.exitonclick()


# Functions into functions (Higher Order Functions - functions that work with other func)
# def add(a, b):
#     return a + b
# def substract(a, b):
#     return a - b

# def calculator(a, b, theFunc):
#     return theFunc(a, b)

# print(calculator(3, 2, add))


#Class and Instance Variables 
"""
# Class for Dog
class Dog:
   
    # Class Variable
    animal = 'dog'            
   
    # The init method or constructor
    def __init__(self, breed, color):
     
        # Instance Variable    
        self.breed = breed
        self.color = color       
    
# Objects of Dog class
Rodger = Dog("Pug", "brown")
Buzo = Dog("Bulldog", "black")
 
print('Rodger details:')  
print('Rodger is a', Rodger.animal)
print('Breed: ', Rodger.breed)
print('Color: ', Rodger.color)
 
print('\nBuzo details:')  
print('Buzo is a', Buzo.animal)
print('Breed: ', Buzo.breed)
print('Color: ', Buzo.color)
 
# Class variables can be accessed using class
# name also
print("\nAccessing class variable using class name")
print(Dog.animal)       
"""