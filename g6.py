import pgzrun


WIDTH = 600
HEIGHT = 500

class Player(Actor):
    speed = 3
    def move(self):
        if keyboard.left:
            self.x -= self.speed
        if keyboard.right:
            self.x += self.speed
        if keyboard.up:
            self.y -= self.speed
        if keyboard.down:
            self.y += self.speed

    def boundary_check(self):
        if self.x > WIDTH:
            self.x = 0
        if self.x < 0:
            self.x = WIDTH
        if self.y > HEIGHT:
            self.y = 0
        if self.y < 0:
            self.y = HEIGHT

class Enemy(Actor):
    pass

class Coin(Actor):
    pass


p = Player('character_0000', pos=(200,100))


def draw():
    screen.clear()
    p.draw()

def update():
    p.move()
    p.boundary_check()


pgzrun.go()
