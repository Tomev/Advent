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


def is_within_region(pos, pts):

    max_distance = 10000
    current_distance = 0

    for pt in pts:
        current_distance += abs(pos.x - pt.x) + abs(pos.y - pt.y)

    return current_distance < max_distance


start_id = 65  # >= 2 for latter array initialization
non_id_char = chr(start_id - 1)
contested_id = chr(start_id - 2)

file_read = open("input.txt", "r")

line = file_read.readline()

points = []
point_id = start_id

# Get points
while line:
    coordinates = line.split(', ')
    points.append(Point(chr(point_id), int(coordinates[0]), int(coordinates[1])))
    point_id += 1
    line = file_read.readline()

# Find boundaries
max_x = min_x = points[0].x
max_y = min_y = points[0].y

for point in points:
    if max_x < point.x:
        max_x = point.x
    if min_x > point.x:
        min_x = point.x
    if max_y < point.y:
        max_y = point.y
    if min_y > point.y:
        min_y = point.y

# Count region area
region_area = 0

for coord_x in range(min_x, max_x + 1):
    for coord_y in range(min_y, max_y + 1):
        position = Point('', coord_x, coord_y)
        if is_within_region(position, points):
            region_area += 1

print(f'The area of this region equals {region_area}.')

