import pygame

screen = None
size = w, h, = 600, 600
pygame.init()
screen = pygame.display.set_mode(size)
class Win:
    def __init__(self):
        self.screen_update()
    def screen_update(self):
        self.run = True
        screen.fill((0,0,0))
        while self.run:
            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    self.run = False

            # DRAWING

            pygame.display.flip()

if __name__ == '__main__':
    win = Win()
