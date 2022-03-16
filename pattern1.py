from turtle import Turtle, Screen
import random

colors = ["black", "orange", "purple", "violet", "cyan", "light green", "dark goldenrod", "pink", "gray"]
new_t = Turtle()


i = 4
while (i <= 12):
    for _ in range(i):
        new_t.forward(100)
        new_t.right(360/i)
    new_t.pencolor(random.choice(colors))
    i += 1


my_screen = Screen()
my_screen.exitonclick()