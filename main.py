from automata.Scenario import Scenario
from automata.character.Character import Character
from automata.ruleset.GameOfLifeRuleset import GameOfLife
from automata.Point import Point
from automata.ruleset.Ruleset import Ruleset
from automata.ruleset.Handstander import Handstander
from automata.ruleset.TupperWasher import TupperWasher
from automata.ruleset.StoneThrower import StoneThrower
from automata.Scenario import scenario as automata
from time import sleep
import random


def main():

    width = 10
    height = 10

    c1 = Character(point=Point(1,1), ruleset=Handstander, team=2)
    c2 = Character(point=Point(1,1), ruleset=TupperWasher, team=2)
    c3 = Character(point=Point(1,1), ruleset=StoneThrower, team=2)
    c4 = Character(point=Point(1,1), ruleset=Handstander, team=1)
    c5 = Character(point=Point(1,1), ruleset=TupperWasher, team=1)
    c6 = Character(point=Point(1,1), ruleset=StoneThrower, team=1)
    # c4 = Character(point=Point(1,0), ruleset=Handstander, team=1)
    # c5 = Character(point=Point(1,1), ruleset=Handstander, team=2)
    # c6 = Character(point=Point(1,1), ruleset=Handstander, team=2)
    # c7 = Character(point=Point(1,1), ruleset=Handstander, team=2)
    # c8 = Character(point=Point(1,0), ruleset=Handstander, team=1)
    # c9 = Character(point=Point(1,0), ruleset=Handstander, team=1)
    # c10 = Character(point=Point(1,0), ruleset=Handstander, team=1)
    # c11 = Character(point=Point(1,0), ruleset=Handstander, team=1)
    # c12 = Character(point=Point(1,0), ruleset=Handstander, team=1)
    chars = [c1,c2,c3,c4,c5,c6]

    for c in chars:
        automata.add_character(c)

    for i in range(1000):
        print("TICK {}\n".format(i))
        automata.renderer.show()

        for c in chars:
            print('Team: {} | Ruleset: {} | Health: {}'.format(c.team, c.hp))
        automata.tick()
        print('\n\n')
        sleep(0.1)


if __name__ == '__main__':
    main()
