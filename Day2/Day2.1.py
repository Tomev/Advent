def has_letter_that_occurs_exactly_n_times(string, n):
    char_set = set(string)

    for char in char_set:
        if string.count(char) == n:
            return True

    return False


file_read = open("input.txt", "r")

line = file_read.readline()

ids_with_letters_occurring_2_times = 0
ids_with_letters_occurring_3_times = 0

while line:

    if has_letter_that_occurs_exactly_n_times(line, 2):
        ids_with_letters_occurring_2_times += 1
    if has_letter_that_occurs_exactly_n_times(line, 3):
        ids_with_letters_occurring_3_times += 1

    line = file_read.readline()

print(f'Checksum: {ids_with_letters_occurring_2_times * ids_with_letters_occurring_3_times}.')


