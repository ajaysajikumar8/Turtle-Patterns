import random
from turtle import Turtle, Screen

is_game_on = False
myscreen = Screen()
myscreen.setup(width = 500,height = 400)
user_bet = myscreen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a colour: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-90,-60,-30,0,30,60]
all_turtles = []

for turtle_index in range(0,6):
    new_tur = Turtle(shape="turtle")
    new_tur.color(colors[turtle_index])
    new_tur.penup()
    new_tur.goto(x=-230,y=y_pos[turtle_index])
    all_turtles.append(new_tur)

if user_bet:
    is_game_on = True

while is_game_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_game_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! the {winning_color} is the winner!")
            else:
                print(f"You've lost! the {winning_color} is the winner!")

        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)

myscreen.exitonclick()
