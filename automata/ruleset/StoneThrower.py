from .Ruleset import Ruleset
from .State import *

class StoneThrower(Ruleset):
    def __init__(self, character):

        super().__init__(character)

        self.handlers = {
            Attacking: [
                {
                    "event": self.attacking_to_running,
                    "next_state": Running
                }
            ],
            Wandering: [
                {
                    "event": self.wandering_to_attacking,
                    "next_state": Attacking
                }
            ],
            Running: [
                {
                    "event": self.running_to_wandering,
                    "next_state": Wandering
                }
            ]
        }

    @property
    def initial(self):
        return Wandering

    def wandering_to_attacking(self):
        return len(self._character.enemies_onpoint(self._character.vicinity)) > 0

    def attacking_to_running(self):
        return len(self._character.enemies_onpoint()) > 0

    def running_to_wandering(self):
        return len(self._character.enemies_onpoint(self._character.vicinity.append(self._character.point))) == 0


    def attack(self):
        print("he attac")

    def wander(self):
        print("he wanderrr")

    def run(self):
        print("he ran")
