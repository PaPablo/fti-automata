class State():
    def do(self, character):
        raise NotImplementedError


class Attacking(State):
    pass

class Wandering(State):
    pass

class Running(State):
    pass


class Ruleset():
    def __init__(self):
        handlers:{
            Attacking: [
            #lista de transiciones
                {
                    #el evento tiene que ser una funcion que recibe un personaje
                    "event": None,
                    "next_state": None
                },
            ]
            Wandering:[
            #lista de transiciones
                {
                    #el evento tiene que ser una funcion que recibe un personaje
                    "event": None,
                    "next_state": None
                },
            ]
            Running:[
            #lista de transiciones
                {
                    #el evento tiene que ser una funcion que recibe un personaje
                    "event": None,
                    "next_state": None
                },
            ]
        }

    def action(self, character, neighbors):
        raise NotImplementedError
