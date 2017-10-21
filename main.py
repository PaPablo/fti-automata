from automata.Scenario import Scenario
from automata.character.Character import Character
from automata.ruleset.GameOfLifeRuleset import GameOfLife
from automata.Point import Point
from automata.ruleset.Ruleset import Ruleset
from automata.Scenario import scenario as automata
import random

def main():

    width = 10
    height = 10

    for w in range(automata.width):
        for h in range(automata.height):
            automata.add_character(
                    Character(
                        point=Point(w,h),
                        ruleset=GameOfLife,
                        team=1,
                        radius=1
                        )

                    )


    for i in range(10):
        print("TICK {}\n".format(i))
        automata.renderer.show()
        automata.tick()
        print('\n\n')
        input()

if __name__ == '__main__':
    main()
