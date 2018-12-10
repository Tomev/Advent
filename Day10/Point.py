from math import sqrt

class Point:
    x = 0
    y = 0
    v_x = 0
    v_y = 0

    def __init__(self, line):
        x = line.split('n=<')[1].split(',')[0]
        self.x = int(x)
        y = line.split(',')[1].split('>')[0]
        self.y = int(y)
        v_x = line.split('y=<')[1].split(',')[0]
        self.v_x = int(v_x)
        v_y = line.split(',')[2].split('>')[0]
        self.v_y = int(v_y)

    def __str__(self):
        return f'r = ({self.x}, {self.y}), v = ({self.v_x}, {self.v_y})'

    def __repr__(self):
        return self.__str__()

    def tick(self):
        self.x += self.v_x
        self.y += self.v_y

    def distance(self, other):
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)
