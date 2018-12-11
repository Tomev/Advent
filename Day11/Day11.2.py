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


assert get_cell_power_level(Point(3, 5), 8) == 4, 'Assertion #0 failed.'
assert get_cell_power_level(Point(122, 79), 57) == -5, 'Assertion #1 failed.'
assert get_cell_power_level(Point(217, 196), 39) == 0, 'Assertion #2 failed.'
assert get_cell_power_level(Point(101, 153), 71) == 4, 'Assertion #3 failed.'


serial_number = 5153
# serial_number = 42
n_level_grids_power_levels = [[[0]], []]

for grid_x in range(0, 300):
    n_level_grids_power_levels[1].append([])
    for grid_y in range(0, 300):
        n_level_grids_power_levels[1][grid_x].append(get_cell_power_level(Point(grid_x, grid_y), serial_number))


def get_nxn_grid_power_level(n, pt):
    global n_level_grids_power_levels

    grid_power_level = 0

    grid_power_level += n_level_grids_power_levels[n - 1][pt.x][pt.y]

    additional_points_offset = n - 1

    for offset in range(0, additional_points_offset):
        grid_power_level += n_level_grids_power_levels[1][pt.x + offset][pt.y + additional_points_offset]
        grid_power_level += n_level_grids_power_levels[1][pt.x + additional_points_offset][pt.y + offset]

    grid_power_level += n_level_grids_power_levels[1][pt.x + additional_points_offset][pt.y + additional_points_offset]

    return grid_power_level


highest_square_power_level = 0
highest_power_level_point = Point()
highest_power_level_grid_edge = 0

for grid_edge in range(2, 300):

    print(grid_edge)
    n_level_grids_power_levels.append([])

    #for y in n_level_grids_power_levels[grid_edge - 1]:
        #print(y)

    for x in range(0, 300 + 1 - grid_edge):
        n_level_grids_power_levels[grid_edge].append([])
        for y in range(0, 300 + 1 - grid_edge):
            current_point = Point(x, y)
            current_square_power_level = get_nxn_grid_power_level(grid_edge, current_point)
            n_level_grids_power_levels[grid_edge][x].append(current_square_power_level)

            if current_square_power_level > highest_square_power_level:
                highest_square_power_level = current_square_power_level
                highest_power_level_point = current_point
                highest_power_level_grid_edge = grid_edge

                print(f'Power level: {current_square_power_level}')
                print(f'Edge: {grid_edge}')
                print(f'Point: {current_point}')

highest_power_level_point.x += 1
highest_power_level_point.y += 1

print(f'Top-left fuel cell of the 3x3 square with the largest total power is {highest_power_level_point} for grid-edge'
      f' size equal {highest_power_level_grid_edge}.')
