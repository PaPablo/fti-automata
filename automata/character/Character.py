""" The base character that acts in the scenario

Has a point (place in the scenario),
and a reference in said scenario

"""
from automata.ruleset.Ruleset import Ruleset
from automata.Scenario import scenario

class Character():
    def __init__(self, point, ruleset, team, radius=1):
        self.radius = radius
        self.point = point
        self.ruleset = ruleset(self)
        self.state = self.ruleset.initial
        self.team = team

    def __str__(self):
        return 'character at {} {}'.format(self.point.x, self.point.y)

    def __repr__(self):
        return 'character at {} {}'.format(self.point.x, self.point.y)

    def is_in_state(self, state):
        return self.state == state

    @property
    def neighbors(self):
        """devuelve los personajes en su vecindad"""
        return scenario.at_points(
            self.point.vicinity(self.radius))


    def characters_onpoint(self):
        return [c for c in scenario.at_points([self.point]) if c != self]

    def enemies_onpoint(self):
        return filter(self.is_allied, self.characters_onpoint())

    def is_allied(self, character):
        return self.team == character.team

    def action(self):
        self.state.do(self)
        return self

    def attack(self):
        self.ruleset.attack(self)

    def wander(self):
        self.ruleset.wander(self)

    def run(self):
        self.ruleset.run(self)
