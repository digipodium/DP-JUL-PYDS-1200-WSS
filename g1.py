import pgzrun # library import

HEIGHT = 500
WIDTH = 600

def draw():
    screen.fill('white')
    screen.draw.text("Hello PYGAME",(WIDTH//2,HEIGHT//2),color='black',)
    screen.draw.text("Example One",(30,30), fontsize=60, color='red',)

pgzrun.go()