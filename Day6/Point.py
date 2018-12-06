class Point:
    sx = 0
    y = 0
    pt_id = ''

    def __init__(self, pt_id, x, y):
        self.x = x
        self.y = y
        self.pt_id = pt_id

    def __str__(self):
        return f'{self.pt_id}:({self.x}, {self.y})'

    def __repr__(self):
        return self.__str__()
