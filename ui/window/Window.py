import pygame

from ui.colors import colors 


pygame.init()

class Window:
    """Window de render del automata"""

    def __init__(self, width, height):
        self.screen_width = width
        self.screen_height = height

        self.screen = pygame.display.set_mode((self.screen_width,self.screen_width))

        pygame.display.set_caption('mucho bites')
        self.clock = pygame.time.Clock()
        self.done = False

        self.number_lines = 10

        self.inner_radius= 20 

        for y in range(1,self.number_lines):
            pygame.draw.line(self.screen, colors['white'], (0,self.screen_height/self.number_lines*y), (self.screen_width,self.screen_height/self.number_lines*y))

            pygame.draw.line(self.screen, colors['white'], (self.screen_width/self.number_lines*y,0), (self.screen_width/self.number_lines*y,self.screen_height))

    def show():
        pygame.display.update()