file_read = open("input.txt", "r")

line = file_read.readline()

freq = 0
frequencies_achieved = [freq]
was_first_double_frequency_found = False
first_double_frequency = 0

while not was_first_double_frequency_found:
    number = int(line[1:])
    if line[0] == '-':
        freq -= int(number)
    else:
        freq += int(number)

    if frequencies_achieved.__contains__(freq) and not was_first_double_frequency_found:
        was_first_double_frequency_found = True
        first_double_frequency = freq

    frequencies_achieved.append(freq)

    print(freq)

    line = file_read.readline()

    if not line:
        file_read = open("input.txt", "r")
        line = file_read.readline()

print(f'First dobule frequency found was {first_double_frequency}.')


