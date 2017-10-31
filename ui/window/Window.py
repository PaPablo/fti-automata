import pygame
from random import randint
import math

from automata.config import SCENARIO_WIDTH, SCENARIO_HEIGHT, WINDOWS_HEIGHT, WINDOWS_WIDTH, X_LINES, Y_LINES, IMAGES_DIR, GAME_SPEED
from ui.window.sprites import sprite_set

from ui.window.colors import colors

from automata.Scenario import scenario as automata
from automata.Point import Point
from automata.ruleset.State import Attacking

def draw_line(attacker, attackee):
    attacker_x = attacker.point.x * WINDOWS_WIDTH/X_LINES + (WINDOWS_WIDTH/SCENARIO_WIDTH)/2
    attacker_y = attacker.point.y * WINDOWS_WIDTH/Y_LINES + (WINDOWS_HEIGHT/SCENARIO_HEIGHT)/2

    attackee_x = attackee.point.x * WINDOWS_WIDTH/X_LINES + (WINDOWS_WIDTH/SCENARIO_WIDTH)/2
    attackee_y = attackee.point.y * WINDOWS_WIDTH/Y_LINES + (WINDOWS_HEIGHT/SCENARIO_HEIGHT)/2

    pygame.draw.line(screen,colors['red'],(attacker_x,attacker_y),(attackee_x,attackee_y))

screen = pygame.display.set_mode((WINDOWS_WIDTH,WINDOWS_HEIGHT))
def run_simulation():

    pygame.init()


    pygame.display.set_caption('mucho bites')
    surface = pygame.Surface((100,100))
    clock = pygame.time.Clock()
    done = False


    inner_radius= 20 

    white = (255,255,255)



    def lines():
        for y in range(1,Y_LINES):
            pygame.draw.line(screen, white, (0,WINDOWS_HEIGHT/Y_LINES*y), (WINDOWS_WIDTH,WINDOWS_HEIGHT/Y_LINES*y))

        for x in range(1,X_LINES):
            pygame.draw.line(screen, white, (WINDOWS_WIDTH/X_LINES*x,0), (WINDOWS_WIDTH/X_LINES*x,WINDOWS_HEIGHT))

    def fit(characters, x,y):

        points = []
        center_x = x * WINDOWS_WIDTH/X_LINES + (WINDOWS_WIDTH/SCENARIO_WIDTH)/2
        center_y = y * WINDOWS_HEIGHT/Y_LINES + (WINDOWS_HEIGHT/SCENARIO_HEIGHT)/2



        for i in range(len(characters)):
            points.append(
                    {
                    # Ubicación en x del elemento i-esimo a encajar en el cuadrao
                    'x':(inner_radius * math.cos(2 * math.pi * i / len(characters)) + center_x),
                    # Coordenada en y
                    'y':(inner_radius * math.sin(2 * math.pi * i / len(characters)) + center_y),
                    # Equipo del personaje en cuestion 
                    'team':characters[i].team,
                    'state':characters[i].state
                    }
                )

        return points

    def draw_character(points):
        
        for p in points:
            draw_sprite(p)

    def draw_sprite(point):
        # Dibuja sprite del personaje
        x_size = 30
        y_size = 30
        print(sprite_set[point['team']][point['state']])
        image = pygame.image.load(IMAGES_DIR+sprite_set[point['team']][point['state']]) 
        image = pygame.transform.scale(image, (x_size,y_size))

        offset_x = (x_size/2)
        offset_y = (y_size/2)

        rect = pygame.Rect(point['x']-offset_x,point['y']-offset_y,x_size,y_size)
        screen.blit(image, rect)



    # MAIN LOOOPyloop

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
                draw_character(points)


        automata.tick()

        clock.tick(GAME_SPEED)

        pygame.display.flip()