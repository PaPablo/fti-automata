import pygame
from random import randint
import math

from automata.config import SCENARIO_WIDTH, SCENARIO_HEIGHT

from ui.window.colors import colors

from automata.Scenario import scenario as automata
from automata.Point import Point

def run_simulation():
    windows_width = 800
    windows_height = 600

    pygame.init()

    screen = pygame.display.set_mode((windows_width,windows_height))

    pygame.display.set_caption('mucho bites')
    surface = pygame.Surface((100,100))
    clock = pygame.time.Clock()
    done = False

    x_lines = SCENARIO_WIDTH +1
    y_lines = SCENARIO_HEIGHT +1

    inner_radius= 20 

    white = (255,255,255)

    def lines():
        for y in range(1,y_lines):
            pygame.draw.line(screen, white, (0,windows_height/y_lines*y), (windows_width,windows_height/y_lines*y))

        for x in range(1,x_lines):
            pygame.draw.line(screen, white, (windows_width/x_lines*x,0), (windows_width/x_lines*x,windows_height))

    def fit(characters, x,y):

        points = []
        center_x = x * windows_width/x_lines + 40
        center_y = y * windows_height/y_lines + 30



        for i in range(len(characters)):
            points.append(
                    (
                    (inner_radius * math.cos(2 * math.pi * i / len(characters)) + center_x),
                    (inner_radius * math.sin(2 * math.pi * i / len(characters)) + center_y),
                    characters[i].team
                    )
                )

        return points

    def draw_points(points):
        
        for p in points:
            pygame.draw.circle(screen, colors[p[2]],(int(p[0]),int(p[1])), 4)

        
        

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            print(event)
        sum = 0

        screen.fill((0,0,0))
        lines()
        for x in range(SCENARIO_WIDTH+1):
            for y in range(SCENARIO_HEIGHT+1):
                characters = automata.at_points(Point(x,y))
                points = fit(characters,x,y)
                draw_points(points)


        automata.tick()

        clock.tick(5)

        pygame.display.flip()


        
