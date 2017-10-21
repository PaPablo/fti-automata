from .Ruleset import Ruleset

class GameOfLife(Ruleset):
    obj = None
    def __init__(self, character):
        pass

    def action(self, character, neighbors):
        nALives = len([n for n in neighbors if n.alive])

        if  nALives > 3 or nALives < 2:
            character.alive = False
        elif nALives == 3:
            character.alive = True
        else:
            character.alive = character.alive
