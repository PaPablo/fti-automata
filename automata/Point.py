class Point():
    def __init__(self, x,y):
        self.x = x
        self.y = y

    def add(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def equal(self, point):
        return self.x == point.x and self.y == point.y

    def vecinity(self, radius):
        return [self.add(Point(x,y)) for x in range(-1,2) for y in range(-1,2) if x != 0 or y != 0]

    def __repr__(self):
        return 'Point at: ({0}, {1})'.format(self.x, self.y)
