from automata.ruleset.State import Attacking,Running,Wandering
from automata.config import TEAM_1,TEAM_2

sprite_set = {
    TEAM_1 : {
        Attacking:'images/storm-trooper-attacking.png',
        Running:'images/storm-trooper-running.png',
        Wandering:'images/storm-trooper-wandering.png'
    },
    TEAM_2 : {
        Attacking:'images/ewok-attacking.png',
        Running:'images/ewok-running.png',
        Wandering:'images/ewok-wandering.png'
    }
}