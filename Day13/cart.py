from Day3.Point import Point


class Cart:
    directions = ['^', '>', 'v', '<']

    x = 0
    y = 0
    direction = 0
    intersection_decider = 0

    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = self.directions.index(direction)
        self.intersection_decider == 0

    def get_position(self):
        return Point(self.y, self.x)

    def get_direction(self):
        return self.directions[self.direction]

    def make_a_turn(self, current_tile_type):
        if current_tile_type == '+':
            self.turn_on_intersection()
        elif current_tile_type == '\\':
            if self.direction == 1 or self.direction == 3:
                self.turn_right()
            else:
                self.turn_left()
        elif current_tile_type == '/':
            if self.direction == 0 or self.direction == self.direction == 2:
                self.turn_right()
            else:
                self.turn_left()

    def turn_left(self):
        self.direction = (self.direction - 1) % len(self.directions)

    def turn_right(self):
        self.direction = (self.direction + 1) % len(self.directions)

    def turn_on_intersection(self):
        if self.intersection_decider == 0:
            self.turn_left()
            self.intersection_decider = 1
        elif self.intersection_decider == 2:
            self.turn_right()
            self.intersection_decider = 0
        else:
            self.intersection_decider += 1

    def move(self, current_tile_type):

        self.make_a_turn(current_tile_type)

        if self.direction == 0:
            self.x -= 1
        elif self.direction == 1:
            self.y += 1
        elif self.direction == 2:
            self.x += 1
        elif self.direction == 3:
            self.y -= 1

