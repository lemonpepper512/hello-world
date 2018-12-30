#First Project!
#For this project we are going to do the same thing we did last time using a function with arguemnts
#Then using a loop to repeat it, but we want to make squares within a cirlce
#We do this by making the turning 'angle' not exactly 90 degrees, maybe 75?

#We are going to take the function we previously created that contains multiple arguments
#only this time we are going to make it loop.
import turtle #This imports the turtle module.

my_turtle=turtle.Turtle()

def my_square():
    my_turtle.forward(100) #Calling the variable n instead of manually inserting the units
    my_turtle.right(90) #turtle turns to the left 90 degrees
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)
    my_turtle.right(90)
    my_turtle.forward(100)

#Here we create a loop that should repeat our called function ten independent times
#Just like defining a function, the loop ends with (): and the code below needs to be indented.
#The 'i' in this loop can actually be called anything, but using 'i' is simple.
for i in range(360):
    my_square()
    my_turtle.right(100)
    
#We are going to use our loop and call it to run 10,000 times!
#We don't necessary need it to run that long, but we want it to try and complete the circle
