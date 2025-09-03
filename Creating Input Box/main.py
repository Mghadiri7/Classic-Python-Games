import pygame
import sys
from inp import Input_box


class Main:
    def __init__(self):
        pygame.init()
        self.game_display = pygame.display.set_mode((400,400))
        pygame.display.set_caption("InputBox")
        self.inps = [Input_box((125, 80), (150, 35), p_h='Name')]
        self.key = None
        self._key = False
        self.clock = pygame.time.Clock()
        self.run()

    def run(self):
        while True:
            self.game_display.fill('white')
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    key_name = pygame.key.name(event.key)
                    self.key = key_name
                    self._key = True
                if event.type == pygame.KEYUP:
                    self.key = None
            for inp in self.inps:
                self._key = inp.update(self.game_display, 
                                       self.key, self._key)
            pygame.display.update()
            self.clock.tick(60)

new_input = Main()
