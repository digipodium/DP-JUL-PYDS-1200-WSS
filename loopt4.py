from turtle import *
speed(0)
for i in range(6):
    penup()
    forward(100)
    pendown()
    left(360/6)
    for i in range(6):
        forward(150)
        left(360/6)
hideturtle()
mainloop()