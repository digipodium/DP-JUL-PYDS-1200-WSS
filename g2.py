import pgzrun

HEIGHT = 500
WIDTH = 800

box = Rect((50,50), (100,100))
box2 = Rect((450,50), (100,100))

def draw():
    screen.fill('white')
    screen.draw.rect(box, 'red') 
    screen.draw.rect(box2, 'blue')

def update():
    box.x += 1
    if box.x > WIDTH:
        box.x = 0
    
    box2.x += -2
    if box2.x < 0:
        box2.x = WIDTH

    if box2.colliderect(box):
        print("Collision")
        box.x += 4
    

pgzrun.go()