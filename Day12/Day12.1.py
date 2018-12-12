file_read = open("test.txt", "r")
# file_read = open("input.txt", "r")

# Store data in dict

rules = dict()

line = file_read.readline()

state = line.split('initial state: ')[1]
state = state[:-1]

line = file_read.readline() # Omit empty line
line = file_read.readline()

while line:
    split_line = line.split(' => ')
    rules[split_line[0]] = split_line[1][0]
    line = file_read.readline()

iterations_num = 20
plants_num = 0
start_offset = 0

for i in range(1, iterations_num + 2):

    plants_num += state.count('#')

    if state[:2].__contains__('#'):
        state = '..' + state
        start_offset += 2

    if state[-3:].__contains__('#'):
        state += '...'

    print(f'{i - 1} state: {state}')

    new_state = '..'

    for j in range(2, len(state) - 2):

        rule_key = ''

        for state_offset in range(- 2, 3):
            rule_key += state[j + state_offset]

        if rule_key in rules:
            new_state += rules[rule_key]
        else:
            #new_state += state[j]
            new_state += '.'

    state = new_state

print(start_offset)
