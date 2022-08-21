from turtle import *
# speed('fastest')
sides = 6
distance = 120
fillcolor('blue')
begin_fill()
for i in range(sides):
    forward(distance)
    left(360/sides)
end_fill()
mainloop()