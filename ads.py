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
score = 0
font.init()
game_font = font.Font(None,50)
text_score = game_font.render("score:"+str(score),True,(0,0,0))
text = game_font.render("You lose", True,(255,0,0))
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
        for i in range(len(snake)- 1,0,-1):
            snake[i].rect.x = snake[i-1].rect.x
            snake[i].rect.y = snake[i-1].rect.y
        self.rect.x +=self.dx
        self.rect.y +=self.dy

        if self.rect.x > 700:
            self.rect.x = 0
        if self.rect.x < 0:
            self.rect.x = 700
        if self.rect.y < 0:
            self.rect.y = 450
        if self.rect.y > 450:
            self.rect.y = 0
        
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

class Apple(GameSprite):
    def __init__(self,pl_image):
        super().__init__(pl_image,0,0)
    
    def respawn(self):
        self.rect.x = randrange(0,650 - sqi_size,sqi_size)
        self.rect.y = randrange(0,400 - sqi_size,sqi_size)

def load_record():
    try:
        with open("record.txt","r") as file:
            return int(file.read())
    except:
        return 0

def save_record(value):
    with open("record.txt","w") as file:
        file.write(str(value))
ragebait = Apple("ragebait.png")
record = load_record()
head = Snake("head.png",200,250)
apple = Apple("apple.png")
clock = time.Clock()
step_time = timer()
snake = [head]
game = True
finish = False
text_score = game_font.render("score: "+str(score),True,(0,0,0))
text_record = game_font.render("record: "+str(record),True,(0,0,0))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        cur_time = timer()
        window.blit(background,(0,0))
        window.blit(text_score,(10,10))
        window.blit(text_record,(10,40))
        head.get_direct()
        if cur_time - step_time >= 0.5:
            head.update()
            step_time = timer()

            if head.rect.colliderect(apple.rect):
                score +=1
                if score > record:
                    record = score
                    save_record(record)
                
                text_score = game_font.render("score:"+str(score),True,(0,0,0))
                text_record = game_font.render("record"+str(record),True,(0,0,0))
                apple.respawn()
                
                last_part = snake[-1]
                new_x,new_y = last_part.rect.x,last_part.rect.y
            
                if head.dx > 0:
                    new_x -=50
                elif head.dx < 0:
                    new_x +=50
                elif head.dy >0:
                    new_y -=50
                elif head.dy <0:
                    new_y +=50
                new_part = Snake("square.png",new_x,new_y)
                snake.append(new_part)
            if head.rect.colliderect(ragebait.rect):
                ragebait.respawn()
                score = score - 1
                text_score = game_font.render("score:"+str(score),True,(0,0,0))
                last_part.remove()
                if head.dx > 0:
                    new_x -=50
                elif head.dx < 0:
                    new_x +=50
                elif head.dy >0:
                    new_y -=50
                elif head.dy <0:
                    new_y +=50
        for part in snake[1:]:
            if head.rect.colliderect(part.rect):
                finish = True
                window.blit(text,(250,200))
                apple.respawn()
        ragebait.draw()
        apple.draw()
        for part in snake:
            part.draw()
        head.draw()
        display.update()
        clock.tick(fps)