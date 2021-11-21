import pygame, sys
from pygame.constants import MOUSEBUTTONDOWN

from pygame.image import load

class Expolsion(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.is_animating = False
        self.hide = False
        self.sprites = []
        for i in range(1,31):
            self.sprites.append(pygame.image.load("./images/explosion/explosion" + str(i) + ".png"))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]
    def animate(self):
        self.is_animating = True
    def show(self):
        return self.hide
    def update(self):
        if self.is_animating == True:
            self.current_sprite += 0.25
            if self.current_sprite >= len(self.sprites):
                self.current_sprite = 0
                self.is_animating = False
                self.hide = False
            self.image = self.sprites[int(self.current_sprite)]
    def if_win(self):
        self.hide = True
#General setup
pygame.init()
clock = pygame.time.Clock()

#Game screen
width = 400
height = 400
screen = pygame.display.set_mode((width, height))

moving_sprites = pygame.sprite.Group()
explosin = Expolsion(100, 100)
moving_sprites.add(explosin)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                explosin.if_win()
                explosin.animate()

    screen.fill((0, 0, 0))
    if explosin.show() == True:
        moving_sprites.draw(screen)
        moving_sprites.update()
    pygame.display.flip()
    clock.tick(60)