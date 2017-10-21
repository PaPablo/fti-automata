""" The base character that acts in the scenario

Has a point (place in the scenario),
and a reference in said scenario

"""
from automata.ruleset.Ruleset import Ruleset
from automata.Scenario import scenario

class Character():
    def __init__(self, point, ruleset, radius=1):
        self.radius = radius
        self.point = point
        self.ruleset = ruleset
        self.state = ruleset.initial

    def __str__(self):
        return 'character at {} {}'.format(self.point.x, self.point.y)

    def is(self, state):
        return self.state == state

    @property
    def neighbors(self):
        """devuelve los personajes en su vecindad"""
        return scenario.at_points(
            self.point.vicinity(self.radius))


    def characters_onpoint

    def action(self):
        self.state.do(self)
        return self


    def attack(self):
        self.ruleset.attack(self)

    def wander(self):
        self.ruleset.wander(self)

    def run(self):
        self.ruleset.run(self)
