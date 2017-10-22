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
                print("TRANSITIONING TO {} ...".format(transition["next_state"].__name__))
                self._character.state = transition["next_state"]
            else:
                print("NOPE")


    def attack(self):
        raise NotImplementedError

    def wander(self):
        raise NotImplementedError

    def run(self):
        raise NotImplementedError
