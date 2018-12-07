class Worker:
    worker_id = 0
    working_on = ''
    time_left = -1

    def __init__(self, wid):
        self.worker_id = wid


def can_step_be_performed(reqs, done):
    for req in reqs:
        if not done.__contains__(req):
            return False

    return True


def get_instruction_time(instr):
    # return ord(instr) - ord('A') + 1
    return 61 + ord(instr) - ord('A')


file_read = open("input.txt", "r")
#file_read = open("test.txt", "r")

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

'''===================== Second Puzzle ====================='''
# I'm basing on puzzle 1 as it gathers data I'll need.

# Initialize workers and reset variables.
WORKERS_NUM = 5
total_time = 0

steps_performed.clear()

workers = []

for i in range(0, WORKERS_NUM):
    workers.append(Worker(i))

steps_to_perform = steps_order

# Now that I've got workers initialized I'll start the workflow.
while len(steps_performed) != len(steps_order):

    # Check which steps can now be performed
    viable_steps = []
    for i in range(0, len(steps_to_perform)):
        if not steps_info.__contains__(steps_to_perform[i]) or \
               can_step_be_performed(steps_info[steps_to_perform[i]], steps_performed):
            viable_steps.append(steps_to_perform[i])

    # Assign work if possible
    for worker in workers:
        if len(viable_steps) == 0:
            break

        if not worker.working_on == '':
            continue

        worker.working_on = viable_steps[0]
        worker.time_left = get_instruction_time(viable_steps[0])
        steps_to_perform = steps_to_perform.replace(viable_steps[0], '', 1)
        viable_steps = viable_steps[1:]

    print(f'Second ', total_time)

    for worker in workers:
        print(f'Worker #{worker.worker_id} working on {worker.working_on}. Time left {worker.time_left}.')

    # Time flow
    total_time += 1

    for worker in workers:
        worker.time_left -= 1

    # Check if some work was finished
    for worker in workers:
        if worker.time_left == 0:
            steps_performed.append(worker.working_on)
            worker.working_on = ''
            worker.time_left = -1

    print(f'Done: {steps_performed}')

print(f'Sleight building took {total_time} seconds.')
