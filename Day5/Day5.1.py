file_read = open("input.txt", "r")

polymer = file_read.readline()
polymer = polymer[:len(polymer) - 1]  # remove new line char

i = 0
was_polymer_reduced = True

while True:

    if abs(ord(polymer[i]) - ord(polymer[i + 1])) == 32:
        polymer = polymer[:i] + polymer[i + 2:]
        was_polymer_reduced = True
    else:
        i += 1

        if i == len(polymer) - 1 and not was_polymer_reduced:
            break

    if i == len(polymer) - 1:
        i = 0
        was_polymer_reduced = False

print(polymer)
print(f'Resulting polymer contains {len(polymer)} units.')
