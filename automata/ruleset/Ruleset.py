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


class Ruleset():
    def __init__(self, character):
        pass
        #current_state = character.state
        #if(current_state(character)):
        #    character.state = current_state.next_state


        #handlers:{
        #    Attacking: [
        #    #lista de transiciones
        #        {
        #            #el evento tiene que ser una funcion que recibe un personaje
        #            "event": None ,
        #            "next_state": None
        #        },
        #    ],
        #    Wandering:[
        #    #lista de transiciones
        #        {
        #            #el evento tiene que ser una funcion que recibe un personaje
        #            "event": None,
        #            "next_state": None
        #        },
        #    ],
        #    Running:[
        #    #lista de transiciones
        #        {
        #            #el evento tiene que ser una funcion que recibe un personaje
        #            "event": None,
        #            "next_state": None
        #        },
        #    ]
        #}



    @property
    def initial(self):
        return State

    def scan(self):
        pass


    def action(self, character, neighbors):
        raise NotImplementedError
