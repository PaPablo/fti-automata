class State():
    
    @classmethod
    def do(cls, character):
        raise NotImplementedError

class Attacking(State):

    @classmethod
    def do(cls, character):
        character.attack()

class Wandering(State):

    @classmethod
    def do(cls, character):
        character.wander()

class Running(State):

    @classmethod
    def do(cls, character):
        character.run()
