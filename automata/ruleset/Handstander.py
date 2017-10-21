from .Ruleset import Ruleset

class Handstander(Ruleset):

    def __init__(self, character):

        handlers: {
            Attacking: [
                {
                    "event": None,
                    "next_state": Wandering
                }
            ],
            Wandering: [
                {
                    "event": None,
                    "next_state": Attacking
                }
            ]
        }
