from pygame import *
back = (0, 0, 255)
window = display.set_mode((1300, 700))

clock = time.Clock()

sy = 3
sx = 3

FPS = 60
game = True

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_y, size_x, player_speed, stepx, stepy):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_y, size_x))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.sx = stepx
        self.sy = stepy




    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed

        if key_pressed[K_s] and self.rect.y < 700 - 140 :
           self.rect.y += self.speed

class Player2(GameSprite):
    def update(self):
        
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed

        if key_pressed[K_DOWN] and self.rect.y < 700 - 140 :
           self.rect.y += self.speed


class Ball(GameSprite):
    def update(self):
        
        self.rect.x += self.sx
        self.rect.y += self.sy
        
        if self.rect.y > 650:
            self.sy *= -1
        if self.rect.y < 0:
            self.sy *= -1



        if sprite.collide_rect(player, self) or sprite.collide_rect(player2, self):

            self.sx *= -1
            self.sx *= 1.2
            self.sy *= 1.2







ball = Ball('Мяч.png', 650, 350, 50, 50, 10, 3, 3)

player = Player('Палка.png', 2, 700 - 140, 39, 136, 15, 0, 0)

player2 = Player2('Палка.png', 1260, 700 - 140, 39, 136, 15, 0, 0)

finish = False

while game:

    for e in event.get(): 
        if e.type == QUIT:
            game = False

    

    if finish != True:

        
        font.init()
        font2 = font.SysFont(None, 36)

        window.fill(back)

        player.reset()
        player.update()

        player2.reset()
        player2.update()

        ball.reset()
        ball.update()

    if ball.rect.x < 0:
        finish = True
        win1 = font2.render('Player2 WIN!!!', 100, (255,255,255))
        window.blit(win1,(600, 350))

    if ball.rect.x > 1250:
        finish = True
        win2 = font2.render('Player1 WIN!!!', 100, (255,255,255))
        window.blit(win2,(500, 320))


        
    clock.tick(FPS)
    display.update()
