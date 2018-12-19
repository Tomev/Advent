from Day3.Point import  Point

def get_clay_positions(input):
    # Get positions
    clay_pos = []

    file_read = open(input, "r")

    line = file_read.readline()

    while line:
        line_clay_position = get_clay_positions_from_line((line))

        for clay_pt in line_clay_position:
            clay_pos.append(clay_pt)

        line = file_read.readline()

    return clay_pos


def get_clay_positions_from_line(line):
    line = line.split(", ")
    clay_pos = []

    if line[0].__contains__('x'):
        x = line[0].split('=')[1]
        y_range = line[1].split('=')[1].split("..")
        for y in range(int(y_range[0]), int(y_range[1]) + 1):
            clay_pos.append(Point(int(x), int(y)))
    else:
        y = line[0].split('=')[1]
        x_range = line[1].split('=')[1].split("..")
        for x in range(int(x_range[0]), int(x_range[1]) + 1):
            clay_pos.append(Point(int(x), int(y)))

    return clay_pos


spring_position = Point(500, 0)
clay_positions = get_clay_positions("test.txt")
# clay_positions = get_clay_positions("input.txt")

# Find lowest x
min_x = clay_positions[0].x

for clay_position in clay_positions:
    if clay_position.x < min_x:
        min_x = clay_position.x

# Normalize clay_positions
for clay_position in clay_positions:
    clay_position.x -= min_x

# Normalize spring position
spring_position.x -= min_x

# Find upper bounds
max_x = clay_positions[0].x
max_y = clay_positions[0].y

for clay_position in clay_positions:
    if clay_position.x > max_x:
        max_x = clay_position.x
    if clay_position.y > max_y:
        max_y = clay_position.y

# Initialize map with sand
water_map = []

for y in range(max_y + 1):
    water_map.append([])
    for x in range(max_x + 1):
        water_map[y].append('.')

# Add spring to map
water_map[spring_position.y][spring_position.x] = '+'

# Add clays
for clay_position in clay_positions:
    water_map[clay_position.y][clay_position.x] = '#'

for y in water_map:
    print(y)












