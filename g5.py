import pgzrun
from random import randint

HEIGHT = 500
WIDTH = 700
score = 0 
player = Actor('character_0000', pos=(WIDTH//2,HEIGHT//2))
item = Actor('character_0008', pos=(50,50))    
speed = 3

music.play('bgmusic')

def draw():
    screen.fill('black')
    player.draw()
    item.draw() 
    screen.draw.text(f'SCORE : {score}', topleft=(10,500-30), color='white')

def update():
    global score # global variable
    # movement control
    if keyboard.left:
        player.x -= speed
    if keyboard.right:
        player.x += speed
    if keyboard.up:
        player.y -= speed
    if keyboard.down:
        player.y += speed
    
    # boundary control
    if player.x > WIDTH:
        player.x = 0
    if player.x < 0:
        player.x = WIDTH
    if player.y > HEIGHT:
        player.y = 0
    if player.y < 0:
        player.y = HEIGHT   

    # collision control
    if player.colliderect(item):
        score += 1
        item.x = randint(0,WIDTH)
        item.y = randint(0,HEIGHT)
        sounds.sound1.play()


pgzrun.go()