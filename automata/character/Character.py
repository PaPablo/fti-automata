""" The base character that acts in the scenario

Has a point (place in the scenario),
and a reference in said scenario

"""
from automata.ruleset.Ruleset import Ruleset


class Character():
    def __init__(self, point, scenario, ruleset,radius=1):
        self.radius = radius
        self.point = point
        self.scenario = scenario
        self.ruleset = ruleset

    @property
    def neighbors(self):
        return self.scenario.at_points(
            self.point.vicinity(self.radius))

    def action(self):
        self.ruleset.action(self, self.neighbors)
        return self

    def __str__(self):
        return 'character at {} {}'.format(self.point.x, self.point.y)