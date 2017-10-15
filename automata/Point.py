class Point():
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        """Compara un punto con otro punto, 
        dos puntos van a ser iguales cuando 
        sus coordenadas (x, y) sean iguales"""
        return self.x == other.x and self.y == other.y

    def add(self, point):
        """Devuelve un nuevo punto, cuyas coordenadas son la suma del punto
        actual (self), y el punto pasado por parametro"""
        return Point(self.x + point.x, self.y + point.y)

    def vicinity(self, radius):
        return [self.add(Point(x,y)) for x in range(-1,2) for y in range(-1,2) if x != 0 or y != 0]

    def __repr__(self):
        return 'Point at: ({0}, {1})'.format(self.x, self.y)
