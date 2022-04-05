from turtle import Turtle, Screen
import random


new_tur = Turtle()
new_tur.pensize(2)
new_tur.speed("fast")

direction = [0,90,180,270]

for _ in range(500):
    new_tur.forward(50)
    new_tur.setheading(random.choice(direction))
    
myscreen = Screen()
myscreen.exitonclick()