from turtle import *

colors = ['red', 'blue', 'green']
pensize(5)
for i in range(70,0,-1):
    pencolor(colors[i%3])
    forward(100)
    left(360/6)
    dot(i*10)

mainloop()
