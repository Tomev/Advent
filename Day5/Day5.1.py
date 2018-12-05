from Day5.polymer_reduction import reduce_polymer

file_read = open("input.txt", "r")

polymer = file_read.readline()
polymer = polymer[:len(polymer) - 1]  # remove new line char

polymer = reduce_polymer(polymer)

print(polymer)
print(f'Resulting polymer contains {len(polymer)} units.')
