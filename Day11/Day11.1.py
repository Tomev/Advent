from Day3.Point import Point


def get_cell_power_level(pt, serial):

    rack_id = pt.x + 10
    power_level = rack_id * pt.y
    power_level += serial
    power_level *= rack_id
    power_level_string = str(power_level)

    if len(power_level_string) < 3:
        power_level = 0
    else:
        power_level = int(power_level_string[len(power_level_string) - 3])

    return power_level - 5


def get_nxn_grid_power_level(n, pt):
    global serial_number

    grid_power_level = 0

    for i in range(0 , n):
        for j in range(0, n):
            grid_power_level += get_cell_power_level(Point(pt.x + i, pt.y + j), serial_number)

    return grid_power_level


highest_square_power_level = 0
highest_power_level_point = Point()
serial_number = 5153
grid_edge = 3

assert get_cell_power_level(Point(3, 5), 8) == 4, 'Assertion #0 failed.'
assert get_cell_power_level(Point(122, 79), 57) == -5, 'Assertion #1 failed.'
assert get_cell_power_level(Point(217, 196), 39) == 0, 'Assertion #2 failed.'
assert get_cell_power_level(Point(101, 153), 71) == 4, 'Assertion #3 failed.'

for x in range(1, 301 - 2):
    for y in range(1, 301 - 2):
        current_point = Point(x, y)
        current_square_power_level = get_nxn_grid_power_level(grid_edge, current_point)

        if current_square_power_level > highest_square_power_level:
            highest_square_power_level = current_square_power_level
            highest_power_level_point = current_point

print(f'Top-left fuel cell of the 3x3 square with the largest total power is {highest_power_level_point}.')
