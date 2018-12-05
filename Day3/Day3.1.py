class Point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __ref__(self):
        return self.__str__()


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

    def __ref__(self):
        return self.__str__()

    def list_of_occupied_sq_inches(self):
        inches_list = []

        for pt_x in range(self.top_left_corner.x, self.bot_right_corner.x):
            for pt_y in range(self.top_left_corner.y, self.bot_right_corner.y):
                inches_list.append(str(Point(pt_x, pt_y)))

        return inches_list


def have_overlapping_xs(claim1, claim2):
    return True


def have_overlapping_ys(claim1, claim2):
    return True


file_read = open("input.txt", "r")

line = file_read.readline()
claims = []

# Parse claims
while line:
    claims.append(Claim(line))
    line = file_read.readline()

sq_inches_already_claimed = set()
sq_inches_claimed_multiple_times = set()

for i in range(0, len(claims)):

    print(f'Processing claim {i}.')

    sq_inches_claimed = claims[i].list_of_occupied_sq_inches()

    for sq_inch in sq_inches_claimed:
        if sq_inches_already_claimed.__contains__(sq_inch):
            sq_inches_claimed_multiple_times.add(sq_inch)

    sq_inches_already_claimed = sq_inches_already_claimed | set(sq_inches_claimed)

print(f'Square inches within multiple claims: {len(sq_inches_claimed_multiple_times)}.')
