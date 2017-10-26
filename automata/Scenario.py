from ui.Render import Render
from .config import SCENARIO_WIDTH, SCENARIO_HEIGHT

class Scenario():
    def __init__(self,width, height):
        self.width = width
        self.height = height
        self.current_moment = []
        self.renderer = Render(self)


    def __iter__(self):
        return iter(self.current_moment)

    def add_character(self, character):
        self.current_moment.append(character)

    def at_points(self,points):
        """Devuelve los personajes en una lista de puntos"""

        if type(points) != list:
            points = [points]

        return [c for c in self.current_moment for p in points if c and c.point == p]

    def tick(self):
        next_moment = []
        if self.current_moment:
            for c in self.current_moment:
                if c:
                    next_moment.append(c.action())

        self.current_moment = next_moment

    def how_many_team(self, points, team):
        """Devuelve la cantidad de personajes del equipo team en el punto"""

        if type(points) is not list:
            points = [points]

        return len([c  for p in points for c in scenario.at_points(p) if c.team == team])

    def __str__(self):
        return 'Scenario'

scenario = Scenario(height = SCENARIO_HEIGHT,
                    width = SCENARIO_WIDTH)
