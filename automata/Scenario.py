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
        return [c for c in self.current_moment for p in points if c.point == p]

    def tick(self):
        next_moment = []
        for c in self.current_moment:
            next_moment.append(c.action())

        self.current_moment = next_moment

    def __str__(self):
        return 'Scenario'

scenario = Scenario(height = SCENARIO_HEIGHT,
                    width = SCENARIO_WIDTH)
