from automata.Scenario import Scenario
from automata.Cell import Cell, GoLCell
from automata.Point import Point
import random

def main():

    width = 10
    height = 10

    automata = Scenario(width, height)

    for w in range(automata.width):
        for h in range(automata.height):
            automata.add_cell(
                    GoLCell(
                        point=Point(w,h),
                        scenario=automata,
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


