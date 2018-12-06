from .Point import Point


class Claim:
    id = -1
    top_left_corner = Point(0, 0)
    bot_right_corner = Point(0, 0)

    def __init__(self, data):
        self.id = int(data.split(' @ ')[0].split('#')[1])
        tl_data = data.split(' @ ')[1].split(':')[0].split(',')
        self.top_left_corner = Point(int(tl_data[0]), int(tl_data[1]))
        br_data = data.split(': ')[1].split('x')
        self.bot_right_corner = Point(int(tl_data[0]) + int(br_data[0]), int(tl_data[1]) + int(br_data[1]))

    def __str__(self):
        return f'Id: {self.id}, tl: {self.top_left_corner}, br: {self.bot_right_corner}.'

    def __repr__(self):
        return self.__str__()

    def list_of_occupied_sq_inches(self):
        inches_list = []

        for pt_x in range(self.top_left_corner.x, self.bot_right_corner.x):
            for pt_y in range(self.top_left_corner.y, self.bot_right_corner.y):
                inches_list.append(str(Point(pt_x, pt_y)))

        return inches_list
