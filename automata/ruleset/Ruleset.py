import random
from automata.Scenario import scenario
from .State import *

class Ruleset():
    def __init__(self, character):
        self._character = character

    @property
    def initial(self):
        raise NotImplementedError

    @property
    def dmg_points(self):
        raise NotImplementedError

    @property
    def hp_initial(self):
        raise NotImplementedError

    def transition(self):
        for transition in self._character.transitions:
            if transition["event"]():
                # print("TRANSITIONING TO {} ...".format(transition["next_state"].__name__))
                self._character.state = transition["next_state"]
            else:
                pass
                # print("NOPE")

    def attack(self):
        # print("he attac")
        enemy = self._character.enemies_onpoint()
        if enemy == []:
            return

        random.choice(enemy).hit(self._character)

    def wander(self):
        # print("he wanderrr")
        self._character.point = random.choice(self._character.vicinity)

    def run(self):

        def team_filter(point):
            return scenario.how_many_team(point, self._character.team)
        
        destination = max(self._character.vicinity, key=team_filter)

        self._character.point = destination


    