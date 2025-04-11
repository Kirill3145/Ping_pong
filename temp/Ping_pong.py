from pygame import *
back = (0, 0, 255)
window = display.set_mode((700, 500))
window.fill(back)
clock = time.Clock()


FPS = 60
game = True

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_y, size_x, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_y, size_x))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

class Player(GameSprite):
    def update(self):
        
        key_pressed = key.get_pressed()
        if key_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed

        if key_pressed[K_d] and self.rect.x < 700 - 80 :
           self.rect.x += self.speed



while game:

    for e in event.get():
        if e.type == QUIT:
            game = False



    clock.tick(FPS)
    display.update()