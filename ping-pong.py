#Главный исполняющий файл игры Ping-pong
from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_d] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
        if keys_pressed[K_a] and self.rect.y > 5:
            self.rect.y -= self.speed

    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_RIGHT] and self.rect.y < win_height - 150:
            self.rect.y += self.speed
        if keys_pressed[K_LEFT] and self.rect.y > 5:
            self.rect.y -= self.speed

win_widtgh = 600
win_height = 500
win = display.set_mode((win_widtgh, win_height))
display.set_caption('Ping-pong')
background = (200, 255, 255)

FPS = 60
clock = time.Clock()
game = True

sprite_player_l = Player('racket.png', 30, 200, 4, 50, 150)
sprite_player_r = Player('racket.png', 520, 200, 4, 50, 150)
sprire_ball = GameSprite('tenis_ball.png', 200, 200, 4, 50, 50)

while game:
    for e in event.get():
            if e.type == QUIT:
                game = False
    win.fill(background)

    sprite_player_l.update_l()
    sprite_player_r.update_r()
    sprire_ball.update()
    sprite_player_l.reset()
    sprite_player_r.reset()
    sprire_ball.reset()

    display.update()
    clock.tick(FPS)
