from Day10.Point import Point


def normalize_points(pts):
    # Normalize them so that min_x and min_y equals 0

    # Find bounds
    max_y = min_y = pts[0].y
    max_x = min_x = pts[0].x

    for pt in pts:
        if pt.x > max_x:
            max_x = pt.x
        if pt.y > max_y:
            max_y = pt.y
        if pt.x < min_x:
            min_x = pt.x
        if pt.y < min_y:
            min_y = pt.y

    for pt in pts:
        pt.x -= min_x

    for pt in pts:
        pt.y -= min_y


def print_board(pts):
    # Find bounds
    min_y = min_x = 0  # Coz of normalization
    max_y = pts[0].y
    max_x = pts[0].x

    for pt in pts:
        if pt.x > max_x:
            max_x = pt.x
        if pt.y > max_y:
            max_y = pt.y

    # Fill empty space
    space = []

    for y in range(min_y, max_y + 1):
        space.append([])
        for x in range(min_x, max_x + 1):
            space[y].append(' ')

    # Add points
    for pt in pts:
        space[pt.y][pt.x] = 'O'

    for x in space:
        print(x)


file_read = open("test.txt", "r")
file_read = open("input.txt", "r")

line = file_read.readline()
points = []

# Parse points
while line:
    points.append(Point(line))
    line = file_read.readline()

wait_time = 0

while True:
    if points[0].distance(points[1]) < 14:  # 14 was found arbitrarily, but on can look for moments when the sum of
                                            # distances is the closest.
        normalize_points(points)
        print_board(points)
        print()
        break

    wait_time += 1
    for point in points:
        point.tick()

print(f'Information appeared after {wait_time} seconds.')

