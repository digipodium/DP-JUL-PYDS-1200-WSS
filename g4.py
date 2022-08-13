import pgzrun

HEIGHT = 500
WIDTH = 500

alieng = Actor('character_0000',topleft=(50,50))
alienb = Actor('character_0002', pos=(300,50))
speed = 3
def draw():
    screen.fill('black')
    alieng.draw()
    alienb.draw()

def update():
    alieng.x += 1
    if alieng.x > WIDTH:
        alieng.x = 0
    if keyboard.left:
        alienb.x -= speed
    if keyboard.right:
        alienb.x += speed
    if keyboard.up:
        alienb.y -= speed
    if keyboard.down:
        alienb.y += speed
    if alienb.colliderect(alieng):
        sounds.sound1.play()
pgzrun.go()
        