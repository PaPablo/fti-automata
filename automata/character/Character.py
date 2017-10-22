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
        self.dmg_points = self.ruleset.dmg_points
        self.team = team
        self.hp = self.ruleset.hp_initial

    def __repr__(self):
        return "character at ({}, {}).\nTEAM: {}.\nSTATE: {}.\nHP: {}".format(
            self.point.x, self.point.y, self.team, self.state.__name__, self.hp)

    @property
    def neighbors(self):
        """devuelve los personajes en su vecindad"""
        return scenario.at_points(
            self.point.vicinity(self.radius))

    @property
    def vicinity(self):
        return self.point.vicinity(self.radius)

    @property
    def transitions(self):
        return self.ruleset.handlers[self.state]

    @property
    def dmg_points(self):
        return self._dmg_points

    @dmg_points.setter
    def dmg_points(self, value):
        self._dmg_points = value

    @property
    def alive(self):
        return True if self.hp > 0 else False

    def characters_onpoint(self, points=None):
        """devuelve los personajes en su mismo punto"""
        if(points == None):
            points = self.point
        if(type(points) != list):
            points = [points]
        return [c for c in scenario.at_points(points) if c != self]

    def enemies_onpoint(self, points=None):
        """devuelve los enemigos en su mismo punto"""
        return [c for c in self.characters_onpoint(points) if not c.is_allied(self)]

    def allies_onpoint(self, points=None):
        """devuelve los aliados en su mismo punto"""
        return [c for c in self.characters_onpoint(points) if c.is_allied(self)]

    def is_allied(self, character):
        return self.team == character.team

    def is_in_state(self, state):
        return self.state == state

    def action(self):
        # print("yo im doing")
        self.state.do(self)
        self.ruleset.transition()
        return self

    def attack(self):
        self.ruleset.attack()

    def wander(self):
        self.ruleset.wander()

    def run(self):
        self.ruleset.run()

    def hit(self, character):
        self.hp -= character.dmg_points
