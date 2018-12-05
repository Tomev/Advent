def only_differs_at_one_char(string1, string2):

    if len(string1) != len(string2):
        return False

    number_of_different_chars = 0

    for i in range(0, len(string2)):
        if string2[i] != string1[i]:
            number_of_different_chars += 1
        if number_of_different_chars > 1:
            return False

    return number_of_different_chars == 1


def find_different_char_position(string1, string2):
    for i in range(0, len(string2)):
        if string2[i] != string1[i]:
            return i
    return -1


file_read = open("input.txt", "r")

ids = []

line = file_read.readline()
while line:
    ids.append(line)
    line = file_read.readline()

for q in range(0, len(ids) - 1):
    for j in range(q, len(ids)):
        if only_differs_at_one_char(ids[q], ids[j]):
            different_char_position = find_different_char_position(ids[q], ids[j])
            print(f'Common letters: { ids[j][:different_char_position] + ids[j][different_char_position + 1:] }.')
