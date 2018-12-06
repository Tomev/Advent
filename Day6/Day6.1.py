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


start_id = 65  # >= 2 for latter array initialization
non_id_char = chr(start_id - 1)
contested_id = chr(start_id - 2)


def get_closest_point_id(pos, pts):
    # According to Manhattan Distance
    closest_point_distance = float("inf")
    closest_point_id = contested_id

    for pt in pts:

        current_distance = abs(pt.x - pos.x) + abs(pt.y - pos.y)

        if current_distance == closest_point_distance:
            closest_point_id = contested_id

        if closest_point_distance > current_distance:
            closest_point_distance = current_distance
            closest_point_id = pt.pt_id

    return closest_point_id


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

# Reduce points to boundaries
for point in points:
    point.x -= min_x
    point.y -= min_y

# Initialize an array representing space with an unused char
space = []

for i in range(min_x, max_x + 1):
    space.append([''])  # Explicit data typing
    space[i-min_x].clear()

    for j in range(min_y, max_y + 1):
        space[i - min_x].append(non_id_char)

# print(f'min_x = {min_x}, max_x = {max_x}, min_y = {min_y}, max_y = {max_y}')

# Add points to space
for point in points:
    space[point.x][point.y] = point.pt_id

# Assign value of the closest point, to each point in space
for i in range(0, len(space)):
    for j in range(0, len(space[i])):
        if space[i][j] != non_id_char:
            continue

        position = Point('', i, j)
        space[i][j] = get_closest_point_id(position, points)

# for sx in space:
#    print(sx)

# Find valid points ids (non infinite areas)
valid_ids = []

for point in points:
    valid_ids.append(point.pt_id)

# print(valid_ids)

for symbol in space[0]:
    if valid_ids.__contains__(symbol):
        valid_ids.remove(symbol)
for symbol in space[len(space) - 1]:
    if valid_ids.__contains__(symbol):
        valid_ids.remove(symbol)
for i in range(0, len(space)):
    if valid_ids.__contains__(space[i][0]):
        valid_ids.remove(space[i][0])
    if valid_ids.__contains__(space[i][len(space[i]) - 1]):
        valid_ids.remove(space[i][len(space[i]) - 1])

# print(valid_ids)

# Initialize counts dict
id_counts = dict()

for point_id in valid_ids:
    id_counts[point_id] = 0

# Find most common char from points
for space_row in space:
    for point_id in valid_ids:
        id_counts[point_id] += space_row.count(point_id)

# print(id_counts)

largest_area = 0

#for sx in space:
#   print(sx)

for point_id in valid_ids:
    if largest_area < id_counts[point_id]:
        largest_area = id_counts[point_id]

print(f'Largest non infinite area is equal to {largest_area}.')




