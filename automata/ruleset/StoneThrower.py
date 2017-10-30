import random
from .Ruleset import Ruleset
from automata.config import STONETHROWER_DMG_POINTS,STONETHROWER_HP_INITIAL
from .State import *

class StoneThrower(Ruleset):
    def __init__(self, character):

        super().__init__(character)

        """Transiciones de estados"""
        self.handlers = {
            Attacking: [
                {
                    "event": self.attacking_to_running,
                    "next_state": Running
                },
                {
                    "event": self.attacking_to_wandering,
                    "next_state": Wandering
                },
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

    @property
    def dmg_points(self):
        return STONETHROWER_DMG_POINTS

    @property
    def hp_initial(self):
        return STONETHROWER_HP_INITIAL

    def wandering_to_attacking(self):
        return len(self._character.enemies_onpoint(self._character.vicinity)) > 0

    def attacking_to_running(self):
        return len(self._character.enemies_onpoint()) > 0

    def attacking_to_wandering(self):
        return len(self._character.enemies_onpoint()) == 0

    def running_to_wandering(self):
        return len(self._character.enemies_onpoint(self._character.vicinity.append(self._character.point))) == 0

    def attack(self):
<<<<<<< HEAD
        # print("he attac")
=======
        """Ataca a un enemigo aleatorio en su vecindad"""
        print("he attac")
>>>>>>> 13f52b81f503549a45970d7e3bdf881950f05fa7

        enemy = self._character.enemies_onpoint(self._character.vicinity)

        if enemy == []:
            return

        random.choice(enemy).hit(self._character)
