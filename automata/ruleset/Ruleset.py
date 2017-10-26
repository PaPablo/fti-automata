import random
from automata.Scenario import scenario
from .State import *

class Ruleset():
    def __init__(self, character):
        self._character = character

    def __str__(self):
        return self.__class__.__name__

    @property
    def initial(self):
        """Devuelve un estado inicial que van a tener todos los personajes del Ruleset"""
        raise NotImplementedError

    @property
    def dmg_points(self):
        """Devuelve los puntos de danio que van a tener todos los personajes del Ruleset"""
        raise NotImplementedError

    @property
    def hp_initial(self):
        """Devuelve el hp inicial que van a tener todos los personajes del Ruleset"""
        raise NotImplementedError

    def transition(self):
        """Realiza la transicion de estados (si es que se cumple el evento)"""
        for transition in self._character.transitions:
            if transition["event"]():
                print("TRANSITIONING TO {} ...".format(transition["next_state"].__name__))
                self._character.state = transition["next_state"]
            else:
                print("NOPE")

    def attack(self):
        """Ataca a un enemigo aleatorio en su mismo punto"""
        print("he attac")

        enemy = self._character.enemies_onpoint()
        if enemy == []:
            return

        random.choice(enemy).hit(self._character)

    def wander(self):
        """Se mueve aleatoriamente"""
        print("he wanderrr")
        self._character.point = random.choice(self._character.vicinity)

    def run(self):
        """Se mueve al punto con mayor cantidad de aliados"""

        def team_filter(point):
            return scenario.how_many_team(point, self._character.team)

        destination = max(self._character.vicinity, key=team_filter)

        self._character.point = destination
