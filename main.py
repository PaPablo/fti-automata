from automata.Scenario import Scenario
from automata.character.Character import Character
from automata.ruleset.GameOfLifeRuleset import GameOfLife
from automata.Point import Point
from automata.ruleset.Ruleset import Ruleset
from automata.ruleset.Handstander import Handstander
from automata.Scenario import scenario as automata
from time import sleep
import random


def main():

    width = 10
    height = 10

    c1 = Character(point=Point(1,1), ruleset=Handstander, team=2)
    c3 = Character(point=Point(1,1), ruleset=Handstander, team=2)
    c4 = Character(point=Point(1,1), ruleset=Handstander, team=2)
    c5 = Character(point=Point(1,0), ruleset=Handstander, team=1)
    c6 = Character(point=Point(1,0), ruleset=Handstander, team=1)
    c7 = Character(point=Point(1,0), ruleset=Handstander, team=1)
    chars = [c1,c3,c4,c5,c6,c7]

    for c in chars:
        automata.add_character(c)

    for i in range(1000):
        print("TICK {}\n".format(i))
        automata.renderer.show()

        for c in chars:
            print('Team: {} | Health: {}'.format(c.team, c.hp))
        automata.tick()
        print('\n\n')
        sleep(0.1)


if __name__ == '__main__':
    main()
