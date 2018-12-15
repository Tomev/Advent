from Day3.Point import Point

class CombatUnit:
    affiliation = ''
    position = Point(0, 0)
    HP  = 200
    attack_power = 3

    def __init__(self, affiliation, x, y):
        self.affiliation = affiliation
        self.HP = 200
        self.attack_power = 3
        self.position = Point(x, y)

    def __str__(self):
        return f'{self.affiliation}:{self.HP}, {self.position}'

    def __repr__(self):
        return self.__str__()


def prepare_combat_from_input(input):
    cmbt = ''

    file_read = open(input, "r")
    # file_read = open("input.txt", "r")

    line = file_read.readline()

    while line:
        cmbt += line
        line = file_read.readline()

    return cmbt.split('\n')

def count_combat_outcome(cmbt):

    number_of_complete_rounds = 0
    units = prepare_units(cmbt)

    while True:

        if is_combat_still_going(units):
            break

        number_of_complete_rounds += 1


    remaining_units_hp = 0

    for unit in units:
        remaining_units_hp += unit.HP

    return number_of_complete_rounds * remaining_units_hp


def prepare_units(cmbt):

    cmbt_units = []

    for y in range(0, len(cmbt)):
        for x in range(0, len(cmbt[y])):
            if cmbt[y][x] == 'E' or cmbt[y][x] == 'G':
                cmbt_units.append(CombatUnit(cmbt[y][x], x, y))

    return cmbt_units

def is_combat_still_going(combat_units):
    units_affiliations = set()

    for unit in combat_units:
        units_affiliations.add(unit.affiliation)

    return len(units_affiliations) != 1

def get_units_sorted_by_turn_order(combat_unit):
    return sorted(combat_unit, key=lambda unit: (unit.position.y, unit.position.x))




def remove_dead_units(combat_units):
    # Has to use mutable methods
    units_to_remove = []

    for i in range(0, len(combat_units)):
        if combat_units[i].HP <= 0:
            units_to_remove.append(combat_units[i])

    for unit in units_to_remove:
        combat_units.remove(unit)





def count_manhattan_distance(pt1, pt2):
    return abs(pt1.x - pt2.x) + abs(pt1.y - pt2.y)

assert count_combat_outcome(prepare_combat_from_input("test1.txt")) == 27730


# for l in combat:
#    print(''.join(l)),
