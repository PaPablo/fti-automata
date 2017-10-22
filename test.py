from automata.Scenario import Scenario
from automata.character.Character import Character
from automata.Point import Point
from automata.ruleset.Ruleset import Ruleset
from automata.ruleset.Handstander import Handstander
from automata.ruleset.StoneThrower import StoneThrower
from automata.ruleset.TupperWasher import TupperWasher
from automata.Scenario import scenario as automata
from automata.ruleset.State import *
import random


def test():
    """Aca van lo tests"""
    c1 = Character(point=Point(0,0),ruleset=Ruleset,team=1)
    c2 = Character(point=Point(0,0),ruleset=Ruleset,team=2)
    c3 = Character(point=Point(0,0),ruleset=Ruleset,team=1)
    c4 = Character(point=Point(1,0),ruleset=Ruleset,team=1)

    for c in [c1,c2,c3,c4]:
        automata.add_character(c)

    print('c1.is_team(c2): {}'.format(c1.is_allied(c2)))
    print('c1.is_team(c3): {}'.format(c1.is_allied(c3)))
    print('c1.characters_onpoint(): {}'.format(c1.characters_onpoint()))
    print('c1.characters_onvicinity(): {}'.format(c1.characters_onpoint(c1.vicinity)))
    print('c1.enemies_onpoint(): {}'.format(c1.enemies_onpoint()))

def test_handstander():
    c1 = Character(point=Point(1,1), ruleset=Handstander, team=1)
    c2 = Character(point=Point(1,1), ruleset=Handstander, team=2)
    c3 = Character(point=Point(1,1), ruleset=Handstander, team=2)
    print(c1)
    for c in [c1]:
        automata.add_character(c)

    print(c1.state.__name__)
    print("c1 is in state {}? {}".format(Attacking.__name__, c1.is_in_state(Attacking)))
    c1.action()
    print(c1.state.__name__)
    print("c1 is in state {}? {}".format(Wandering.__name__, c1.is_in_state(Wandering)))


    # for transition in c1.transitions:
    #     if transition["event"]():
    #         print("TRANSITIONING TO {} ...".format(transition["next_state"].__name__))
    #     else:
    #         print("NOPE, THERE ARE {} ENEMIES IN MY POINT".format(len(c1.enemies_onpoint())))

def test_stonethrower():
    c1 = Character(point=Point(1,1), ruleset=StoneThrower, team=1)
    c2 = Character(point=Point(1,2), ruleset=StoneThrower, team=2)
    c3 = Character(point=Point(1,1), ruleset=Handstander, team=2)

    for c in [c1,c2, c3]:
        automata.add_character(c)

    print(c1.ruleset)
    print(c1.state.__name__)
    print("c1 is in state {}? {}".format(Wandering.__name__, c1.is_in_state(Wandering)))
    c1.action()

    print(c1.state.__name__)
    print("c1 is in state {}? {}".format(Attacking.__name__, c1.is_in_state(Attacking)))
    c1.action()


    print(c1.state.__name__)
    print("c1 is in state {}? {}".format(Running.__name__, c1.is_in_state(Running)))

def test_tupperwasher():
    c1 = Character(point=Point(1,1), ruleset=TupperWasher, team=1)
    c2 = Character(point=Point(1,2), ruleset=TupperWasher, team=2)
    c3 = Character(point=Point(1,1), ruleset=TupperWasher, team=1)
    c4 = Character(point=Point(1,1), ruleset=TupperWasher, team=1)
    c5 = Character(point=Point(1,1), ruleset=TupperWasher, team=1)
    # c5 = Character(point=Point(1,1), ruleset=TupperWasher, team=1)

    for c in [c1,c2,c3,c4,c5]:
        automata.add_character(c)

    print(c1.ruleset)
    print(c1.state.__name__)
    print("c1 is in state {}? {}".format(Running.__name__, c1.is_in_state(Running)))
    c1.action()

    print(c1.state.__name__)
    print("c1 is in state {}? {}".format(Attacking.__name__, c1.is_in_state(Attacking)))
    c1.action()


    print(c1.state.__name__)
    print("c1 is in state {}? {}".format(Running.__name__, c1.is_in_state(Running)))

def test_attack():
    c1 = Character(point=Point(1,1), ruleset=Handstander, team=1)
    c2 = Character(point=Point(1,1), ruleset=TupperWasher, team=2)

    chars = [c1,c2]

    for c in chars:
        print(c)
        automata.add_character(c)


    print("\n\n")

    for c in chars:
        c.action()
        print(c)





if __name__ == '__main__':
    # test()
    # test_stonethrower()
    # test_tupperwasher()
    test_attack()
