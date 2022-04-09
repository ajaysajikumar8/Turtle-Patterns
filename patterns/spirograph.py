from turtle import Turtle, Screen
import random
import turtle as t 

new_tur = Turtle()
new_tur.speed("fastest")
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color

def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        new_tur.color(random_color())
        new_tur.circle(100)
        current_heading = new_tur.heading()
        new_tur.setheading(current_heading + size_of_gap)
    
draw_spirograph(6)
myscreen = Screen()
myscreen.exitonclick()
