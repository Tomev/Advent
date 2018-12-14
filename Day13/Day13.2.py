from Day13.cart import Cart
from Day3.Point import Point


def are_on_same_positions(cart1, cart2):
    if cart1.x == cart2.x and cart2.y == cart1.y:
        return True

    return False


def are_any_two_carts_in_same_position(current_carts):
    for cart_i in range(0, len(current_carts)):
        for cart_j in range(cart_i + 1, len(current_carts)):
            if are_on_same_positions(current_carts[cart_i], current_carts[cart_j]):
                print(f'Point of crash {current_carts[cart_i].get_position()}.')
                return True
    return False


def remove_colliding_carts(current_carts):

    carts_to_remove = set()

    for cart_i in range(0, len(current_carts)):
        for cart_j in range(cart_i + 1, len(current_carts)):
            if are_on_same_positions(current_carts[cart_i], current_carts[cart_j]):
                carts_to_remove.add(cart_j)
                carts_to_remove.add(cart_i)

    carts_to_remove = list(carts_to_remove)
    carts_to_remove.sort(reverse=True)

    for cart_index in carts_to_remove:
        print(f'Removing cart {cart_index}.')
        del current_carts[cart_index]


def get_track_moving_order(carts_on_tracks):

    order = []

    for track_y in range(len(carts_on_tracks)):
        for track_x in range(len(carts_on_tracks[track_y])):
            if is_a_cart(carts_on_tracks[track_y][track_x]):
                order.append(Point(track_x, track_y))

    return order


def is_a_cart(tested_char):
    return tested_char == '>' or tested_char == '<' or tested_char == 'v' or tested_char == '^'


file_read = open("test2.txt", "r")
file_read = open("input.txt", "r")

# Parse input.
tracks = []
line = file_read.readline()
i = 0
while line:
    tracks.append([])

    for char in line:
        tracks[i].append(char)

    i += 1
    line = file_read.readline()

# Get carts and prepare empty track.

carts = []

for x in range(0, len(tracks)):
    for y in range(0, len(tracks[x])):
        if tracks[x][y] == '^' or tracks[x][y] == 'v':
            carts.append(Cart(x, y, tracks[x][y]))
            tracks[x][y] = '|'
        if tracks[x][y] == '>' or tracks[x][y] == '<':
            carts.append(Cart(x, y, tracks[x][y]))
            tracks[x][y] = '-'

#for line in tracks_with_carts:
#    print(''.join(line), end=' '),

# Start main loop

i = 0

while len(carts) > 1:

    tracks_with_carts = []

    for line in tracks:
        tracks_with_carts.append(line[:])

    for cart in carts:
        tracks_with_carts[cart.x][cart.y] = cart.get_direction()

    carts_moving_order = get_track_moving_order(tracks_with_carts)

    # for line in tracks_with_carts:
    # print(''.join(line), end=' '),

    # print()

    i += 1
    if i % 1000 == 0:
        print(i)

    for cart_position in carts_moving_order:
        for cart in carts:
            if cart.y == cart_position.x and cart.x == cart_position.y:
                # print(f'Before {cart.x}, {cart.y}, {cart.direction}')
                cart.move(tracks[cart.x][cart.y])
                # print(f'After {cart.x}, {cart.y}, {cart.direction}')
                remove_colliding_carts(carts)

    # for line in tracks_with_carts:
        # print(''.join(line), end=' '),

    # print()

print(f'Last cart position is {carts[0].get_position()}.')
