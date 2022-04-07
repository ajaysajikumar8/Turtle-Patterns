
import random
from turtle import *
import turtle

new_tur = Turtle()
new_tur.pensize(2)
new_tur.speed("fast")
turtle.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

direction = [0,90,180,270]

for _ in range(500):
    new_tur.color(random_color())
    new_tur.forward(50)
    new_tur.setheading(random.choice(direction))
    
myscreen = Screen()
myscreen.exitonclick()
