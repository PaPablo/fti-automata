from .Character import Character
from automata.ruleset.GameOfLifeRuleset import GameOfLife
import random

class GoLCharacter(Character):
    def __init__(self, point, radius, ruleset=GameOfLife()):
        self.alive = bool(random.randint(0,1))

        super(GoLCharacter,self).__init__(point, ruleset, radius)

    def __str__(self):
        return 'character at {} {}'.format(self.point.x, self.point.y)

