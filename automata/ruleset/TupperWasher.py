from .Ruleset import Ruleset
from .State import *
from automata.config import TUPPERWASHER_DMG_POINTS, TUPPERWASHER_HP_INITIAL
class TupperWasher(Ruleset):
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
                },
                {
                    "event": self.running_to_attacking,
                    "next_state": Attacking
                }
            ]
        }

    @property
    def initial(self):
        return Running

    @property
    def dmg_points(self):
        return TUPPERWASHER_DMG_POINTS

    @property
    def hp_initial(self):
        return TUPPERWASHER_HP_INITIAL

    def wandering_to_attacking(self):
        return len(self._character.allies_onpoint()) >= 3

    def running_to_attacking(self):
        return len(self._character.allies_onpoint()) >= 3

    def running_to_wandering(self):
        return len(self._character.enemies_onpoint(self._character.vicinity.append(self._character.point))) == 0

    def attacking_to_running(self):
        return len(self._character.allies_onpoint()) < 3

