def can_step_be_performed(reqs, done):
    for req in reqs:
        if not done.__contains__(req):
            return False

    return True


file_read = open("input.txt", "r")

line = file_read.readline()

# Fill steps info
steps_info = dict()

while line:
    symbol = line.split('before step ')[1][0]
    requirement = line.split('Step ')[1][0]

    if not steps_info.__contains__(symbol):
        steps_info[symbol] = []

    steps_info[symbol].append(requirement)

    line = file_read.readline()

# for key in steps_info:
#    print(f'{key}: [{steps_info[key]}]')

# Find step that doesn't have requirements. That will be first step.
steps_order = ''

all_requirements = set()
all_requiring_steps = set()
steps_that_can_be_initially_performed = []

for key in steps_info:
    all_requiring_steps.add(key)
    all_requirements = all_requirements | set(steps_info[key])

steps_that_can_be_initially_performed = list(all_requirements.difference(all_requiring_steps))
steps_that_can_be_initially_performed.sort()

# print(all_requirements)
# print(all_requiring_steps)
# print(steps_that_can_be_initially_performed)

# Alphabetically add initial steps to order and to performed steps
steps_performed = []

for step in steps_that_can_be_initially_performed:
    steps_order += step
    steps_performed.append(step)

# Find order of the rest
was_all_steps_fired = False
i = 0
keys = [k for k in steps_info]

steps_that_can_be_performed_now = []

while len(keys) > 0:
    if can_step_be_performed(steps_info[keys[i]], steps_performed):
        steps_that_can_be_performed_now.append(keys[i])

    i += 1

    if i >= len(keys):
        steps_that_can_be_performed_now.sort()
        steps_performed.append(steps_that_can_be_performed_now[0])
        steps_order += steps_that_can_be_performed_now[0]
        keys.remove(steps_that_can_be_performed_now[0])
        steps_that_can_be_performed_now.clear()
        i = 0


print(f'Steps have to be completed in following order: {steps_order}.')


