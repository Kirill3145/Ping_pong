from pygame import *
back = (0, 0, 255)
window = display.set_mode((700, 500))

clock = time.Clock()


FPS = 60
game = True

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_y, size_x, player_speed, step_x, step_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_y, size_x))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.step.x = step_x
        self.step.y = step_y


    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if key_pressed[K_s] and self.rect.y < 500 - 140 :
           self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if key_pressed[K_DOWN] and self.rect.y < 500 - 140 :
           self.rect.y += self.speed


class Ball(GameSprite):
    def update(self):
        self.rect.x += self.step
        self.rect.y += self.step
        
        if self.rect.y > 450:
            self.step *= -1
        if self.rect.y < 0:
            self.step *= -1
        if self.rect.x < 0:
            self.step *= -1
        if self.rect.x > 650:
            self.step *= -1

            



ball = Ball('Мяч.png', 350, 250, 50, 50, 10, 3,)

player = Player('Палка.png', 2, 500 - 139, 39, 136, 10, 0, 0)

player2 = Player2('Палка.png', 660, 500 - 139, 39, 136, 10, 0, 0)

finish = False

while game:

    for e in event.get(): 
        if e.type == QUIT:
            game = False


    if finish != True:

        window.fill(back)

        player.reset()
        player.update()

        player2.reset()
        player2.update()

        ball.reset()
        ball.update()
        
    clock.tick(FPS)
    display.update()


    clock.tick(FPS)
    display.update()
