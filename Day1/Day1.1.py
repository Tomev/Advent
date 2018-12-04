file_read = open("input.txt", "r")

line = file_read.readline()

freq = 0

while line:
    number = int(line[1:])
    if line[0] == '-':
        freq -= int(number)
    else:
        freq += int(number)

    line = file_read.readline()

    print(f'Current freq = {freq}')


