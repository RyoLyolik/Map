import pygame
import os
import sys, requests
from func import Mapping

size = w, h, = 600, 450
pygame.init()
screen = pygame.display.set_mode(size)
mapping = Mapping()
class Win:
    def __init__(self):
        self.group = pygame.sprite.Group()
        self.screen_update()
    def screen_update(self):
        self.run = True
        self.map_image = self.load_map(mapping.start())
        self.map_now = pygame.sprite.Sprite()
        self.map_now.image = self.map_image
        self.map_now.rect = self.map_now.image.get_rect()
        self.group.add(self.map_now)
        while self.run:
            screen.fill((0, 0, 0))
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.run = False

            self.group.draw(screen)

            pygame.display.flip()

    def load_map(self, name):
        fullname = os.path.join(name)
        try:
            image = pygame.image.load(fullname)
        except pygame.error as message:
            print('Cannot load image: ', name)
            raise SystemExit(message)
        print(image)
        image = image.convert_alpha()
        return image


if __name__ == '__main__':
    win = Win()
