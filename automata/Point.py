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
        return [self.add(Point(x,y))
            for x in _radius
            for y in _radius
            if x != 0 or y != 0]

    def __repr__(self):
        return 'Point at: ({0}, {1})'.format(self.x, self.y)
