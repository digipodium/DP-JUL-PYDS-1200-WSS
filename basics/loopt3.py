from turtle import *
speed(0)
pencolor('red')
bgcolor('yellow')
val = 1
while True:
    forward(5 * val)
    left(360/5)
    circle(50,50)
    val += 1
