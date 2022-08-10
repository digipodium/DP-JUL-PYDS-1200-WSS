import pgzrun

HEIGHT = 500
WIDTH = 500

sun = Actor('sun1', pos=(200,200))
poke = Actor('pika', topleft=(0, 0)) 

def draw():
    screen.fill('white')
    sun.draw()
    poke.draw()

def update():
    sun.y += 1
    if sun.y > HEIGHT:
        sun.y = 0

pgzrun.go()