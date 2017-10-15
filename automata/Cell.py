""" The base cell that acts in the scenario

Has a point (place in the scenario),
and a reference in said scenario

"""
import random

class Ruleset():
    def action(self):
        pass

class GameOfLife():
    obj = None
    def __init__(self):
        pass

    def action(self, cell, scenario):
        neighborhood = scenario.atPoints(cell.point.vicinity(cell.radius))
        nALives = len([n for n in neighborhood if n.alive])

        if  nALives > 3 or nALives < 2:
            cell.alive = False
        elif nALives == 3:
            cell.alive = True
        else:
            cell.alive = cell.alive

class Cell():
    def __init__(self, point, scenario, ruleset,radius=1):
        self.radius = radius
        self.point = point
        self.scenario = scenario
        self.ruleset = ruleset

    def neighbors(self):
        return self.point.vicinity(self.radius)

    def action(self):
        self.ruleset.action(self, self.scenario)
        return self

    def __str__(self):
        return 'cell at {} {}'.format(self.point.x, self.point.y)

class GoLCell(Cell):
    def __init__(self, point, scenario, radius, ruleset=GameOfLife()):
        self.alive = random.random() < 0.3

        super(GoLCell,self).__init__(point, scenario,ruleset, radius)

    def __str__(self):
        return 'cell at {} {}'.format(self.point.x, self.point.y)

