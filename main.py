from automata.Scenario import Scenario
from automata.character.Character import Character
from automata.character.GoLCharacter import GoLCharacter
from automata.Point import Point
from automata.ruleset.Ruleset import Ruleset
from automata.Scenario import scenario as automata
import random

# def main():
# 
#     width = 10
#     height = 10
# 
#     for w in range(automata.width):
#         for h in range(automata.height):
#             automata.add_character(
#                     GoLCharacter(
#                         point=Point(w,h),
#                         radius=1
#                         )
# 
#                     )
# 
#     
#     for i in range(10): print("TICK {}\n".format(i))
#         automata.renderer.show()
#         automata.tick()
#         print('\n\n')
#         input()

def test():
    """Aca van lo tests"""
    c1 = Character(point=Point(0,0),ruleset=Ruleset,team=1)
    c2 = Character(point=Point(0,0),ruleset=Ruleset,team=2)
    c3 = Character(point=Point(0,0),ruleset=Ruleset,team=1)

    for c in [c1,c2,c3]:
        automata.add_character(c)

    print('c1.is_team(c2): {}'.format(c1.is_allied(c2)))
    print('c1.is_team(c3): {}'.format(c1.is_allied(c3)))
    print('c1.characters_onpoint(): {}'.format(c1.characters_onpoint()))
    print('c1.enemies_onpoint(): {}'.format(c1.enemies_onpoint()))

if __name__ == '__main__':
    #main()
    test()


