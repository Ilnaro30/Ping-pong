#Главный исполняющий файл игры Ping-pong
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_d] and self.rect.x < win_widtgh - 80:
            self.rect.x += self.speed
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed

class Enemy(GameSprite):
    def update(self):
        global lost
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.y = 0
            self.rect.x = randint(80, win_widtgh - 80)
            lost += 1

win_widtgh = 600
win_height = 500
win = display.set_mode((win_widtgh, win_height))

display.set_caption('Ping-pong')
background = (200, 255, 255)
win.fill(background)

FPS = 60
clock = time.Clock()
game = True

while game:
    for e in event.get():
            if e.type == QUIT:
                game = False
    display.update()
    clock.tick(FPS)
