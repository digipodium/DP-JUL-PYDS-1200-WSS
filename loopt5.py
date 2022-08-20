from turtle import *
speed(0)
def hexagon(size,pc):
    fillcolor(pc)
    begin_fill()
    for i in range(6):
        forward(size * 5)
        left(360/6)
    end_fill()


colors = ['red', 'blue', 'green']
i = 50
while True:
    hexagon(i, colors[i%3])
    i -= 1
    if i < 0:
        break

mainloop()