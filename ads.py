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

head = GameSprite("head.png",200,250)
clock = time.Clock()

game = True
finish = False

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:

        window.blit(background,(0,0))

        head.draw()

        display.update()
        clock.tick(fps)