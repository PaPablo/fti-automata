from automata.Automata import Automata, Cell
from automata.Point import Point

def main():
    auto = Automata([Cell(Point(x,y)) for x in range(10) for y in range(10)])

    a = auto.tick()

    print(a)
if __name__ == '__main__':
    main()