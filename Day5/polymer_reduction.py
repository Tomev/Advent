def reduce_polymer(poly):
    i = 0
    was_polymer_reduced = True

    while True:

        if i >= len(poly) - 1:
            i = 0
            was_polymer_reduced = False

        if abs(ord(poly[i]) - ord(poly[i + 1])) == 32:
            poly = poly[:i] + poly[i + 2:]
            was_polymer_reduced = True
        else:
            i += 1

            if i == len(poly) - 1 and not was_polymer_reduced:
                break

    return poly
