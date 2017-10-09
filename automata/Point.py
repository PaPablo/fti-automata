class Point():
    def __init__(self, x,y):
        self.x = x
        self.y = y
    
    def add(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def __repr__(self):
        return 'Point at: ({0}, {1})'.format(self.x, self.y)