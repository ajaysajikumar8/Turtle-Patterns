from turtle import Turtle, Screen

new_tur = Turtle()
myscreen = Screen()

def move_forwards():
    new_tur.forward(10)

def move_backwards():
    new_tur.backward(10)

def turn_left():
    new_heading = new_tur.heading() + 10
    new_tur.setheading(new_heading)

def turn_right():
    new_heading = new_tur.heading() - 10
    new_tur.setheading(new_heading)

def clear():
    new_tur.clear()
    new_tur.penup()
    new_tur.home()
    new_tur.pendown()

myscreen.listen()
myscreen.onkey(fun=move_forwards, key="w")
myscreen.onkey(fun=move_backwards, key="s")
myscreen.onkey(fun=turn_left, key="a")
myscreen.onkey(fun=turn_right, key="d")
myscreen.onkey(fun=clear, key="c")

myscreen.exitonclick()
