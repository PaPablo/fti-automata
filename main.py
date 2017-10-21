from automata.Scenario import Scenario
from automata.character.Character import Character
from automata.character.GoLCharacter import GoLCharacter
from automata.Point import Point
from automata.Scenario import scenario as automata
import random

def main():

    width = 10
    height = 10


    for w in range(automata.width):
        for h in range(automata.height):
            automata.add_character(
                    GoLCharacter(
                        point=Point(w,h),
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


