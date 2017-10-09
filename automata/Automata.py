class Cell():
    def __init__(self, point, kind=None):
        self.point = point

    def action(self):
        print('action {0} {1} '.format(self.point.x, self.point.y))
        return self

class Automata():
    def __init__(self,cells):
        self.current_moment = cells

    def tick(self):
        next_moment = []
        for c in self.current_moment:
            next_moment.append(c.action())
        
        self.current_moment = next_moment

    def __repr__(self):
        return self.current_moment