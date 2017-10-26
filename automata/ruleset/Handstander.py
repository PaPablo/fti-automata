import random
from .Ruleset import Ruleset
from .State import *
from automata.config import HANDSTANDER_DMG_POINTS, HANDSTANDER_HP_INITIAL



class Handstander(Ruleset):

    def __init__(self, character):

        super().__init__(character)


        self.handlers = {
            Attacking: [
                {
                    "event": self.attacking_to_wandering,
                    "next_state": Wandering
                }
            ],
            Wandering: [
                {
                    "event": self.wandering_to_attacking,
                    "next_state": Attacking
                }
            ]
        }


    def attacking_to_wandering(self):
        """No hay enemigos en nuestro punto"""
        return len(self._character.enemies_onpoint()) == 0

    def wandering_to_attacking(self):
        """Hay por lo menos un enemigo en nuestro punto"""
        return len(self._character.enemies_onpoint()) > 0

    @property
    def initial(self):
        return Attacking

    @property
    def dmg_points(self):
        return HANDSTANDER_DMG_POINTS

    @property
    def hp_initial(self):
        return HANDSTANDER_HP_INITIAL
