from automata.Point import Point
from automata.ruleset.State import *

class Render():
    def __init__(self, scenario):
        self.scenario = scenario
        self.representation = [[0] * scenario.width for y in [x for x in range(scenario.height)]]

        self.states = {
            Attacking:'A',
            Wandering:'W',
            Running:'R'
        }

    def show(self):
        for w in range(self.scenario.width):
            for h in range(self.scenario.height):
                character = self.scenario.at_points([Point(h,w)])
                if character:
                    for c in character:
                        if c.alive:
                            self.representation[w][h] = self.states[c.state]

                        else:
                            self.representation[w][h] = 0
                else:
                    self.representation[w][h] = 0

        for y in self.representation:
            print(' '.join(str(x) for x in y))


