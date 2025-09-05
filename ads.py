from pygame import *
from time import time as timer
from random import *
sqi_size = 50
width = 750
height = 500
fps = 60 

window = display.set_mode((width,height))
display.set_caption("snake")
background = transform.scale(image.load("background.jpg"), (width,height))

class GameSprite(sprite.Sprite):
    def __init__(self,pl_image,x,y):
        super().__init__()
        self.image = transform.scale(image.load(pl_image), (sqi_size,sqi_size))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self):
        window.blit(self.image,(self.rect.x,self.rect.y))

class Snake(GameSprite):
    def __init__(self,pl_image,x,y):
        super().__init__(pl_image,x,y)
        self.dx = sqi_size
        self.dy = 0
    def update(self):
        self.rect.x +=self.dx
        self.rect.y +=self.dy
    def get_direct(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.dy == 0:
            self.dx = 0
            self.dy = -sqi_size
        elif keys[K_DOWN] and self.dy == 0:
            self.dx = 0
            self.dy = sqi_size
        elif keys[K_LEFT] and self.dx == 0:
            self.dx = -sqi_size
            self.dy = 0
        elif keys[K_RIGHT] and self.dx == 0:
            self.dx = sqi_size
            self.dy = 0

head = Snake("head.png",200,250)
clock = time.Clock()
step_time = timer()

game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        cur_time = timer()
        window.blit(background,(0,0))
        
        head.get_direct()
        if cur_time - step_time >= 0.5:
            head.update()
            step_time = timer()
        head.draw()
        display.update()
        clock.tick(fps)