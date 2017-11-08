# Trabajo Final - Fundamentos de Informática 2017

## De Ewoks, Stormtroopers y Autómatas Celulares

Simulación  del contraataque de la [Batalla de Endor](http://starwars.wikia.com/wiki/Battle_of_Endor) mediante autómatas celulares. Cada tipo de personaje, con sus reglas, representado por un autómata finito distinto.

Implementada en [Python](https://www.python.org/) y [Pygame](http://pygame.org/)

A saber:

* HandStander: Ataca si tiene enemigos en su mismo punto. Se va a mover al punto vecino con menos enemigos. Si está solo, se mueve aleatoriamente.

* StoneThrower: Se escapa hacia donde haya menos enemigos, ataca solamente a un punto vecino si no tiene enemigos en su punto.

* TupperWasher: Se va a mover al punto con mayor cantidad de aliados. Ataca si está con tres o más aliados en su vecindad.

## Cómo correrlo?

1. Clonar el repo
2. Instalar el contenido del requirements.txt
3. En `config.py` en la variable `IMAGES_DIR` colocar la ruta al repo
3. `python main.py`
