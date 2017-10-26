from .config import SCENARIO_HEIGHT, SCENARIO_WIDTH


class Point():
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        """Se compara con otro punto,
        dos puntos van a ser iguales cuando
        sus coordenadas (x, y) sean iguales"""
        if(not isinstance(other, Point)):
            return False

        return self.x == other.x and self.y == other.y

    def add(self, point):
        """Devuelve un nuevo punto, cuyas coordenadas
        son la suma sus coordenadas, y el punto pasado por parametro"""
        return Point(self.x + point.x, self.y + point.y)

    def vicinity(self, radius):
        """Devuelve sus puntos vecinos en un rango especificado"""
        _radius = range(-radius, radius+1)
        return [p for p in [self.add(Point(_x,_y))
            for _x in _radius
            for _y in _radius
            if (_x != 0 or _y != 0)]
            if (p.x >= 0 and p.x <= SCENARIO_WIDTH) and
            (p.y >= 0 and p.y <= SCENARIO_HEIGHT)]



    def __repr__(self):
        return 'Point at: ({0}, {1})'.format(self.x, self.y)
