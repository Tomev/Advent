from datetime import datetime


class ElfGuard:
    id = -1
    time_asleep = 0

    def __init__(self, guard_id):
        self.id = guard_id

    def __str__(self):
        return f'id: {self.id}, sleep time: {self.time_asleep}.'

    def __ref__(self):
        return self.__str__()


file_read = open("input.txt", "r")
#file_read = open("test.txt", "r")

line = file_read.readline()

times_and_events = dict()

# Prepare input to be chronologically sorted
while line:

    events_date_and_time = line.split('[')[1].split(']')[0]
    events_date = events_date_and_time.split(' ')[0].split('-')
    events_time = events_date_and_time.split(' ')[1].split(':')

    event = line.split('] ')[1]

    times_and_events[datetime(int(events_date[0]), int(events_date[1]), int(events_date[2]),
                              int(events_time[0]), int(events_time[1]))] = event

    line = file_read.readline()


elf_guards_data = dict()
current_guard_id = -1

sleep_start = 0

for key in sorted(times_and_events):

    # print(f'{str(key)}: {times_and_events[key]}')

    if times_and_events[key].__contains__('#'):
        current_guard_id = int(times_and_events[key].split('#')[1].split(' ')[0])
        sleep_start = 0

        if not elf_guards_data.__contains__(current_guard_id):
            elf_guards_data[current_guard_id] = ElfGuard(current_guard_id)

    if times_and_events[key].__contains__('falls'):
        sleep_start = key.minute

    if times_and_events[key].__contains__('wakes'):
        elf_guards_data[current_guard_id].time_asleep += key.minute - sleep_start

most_time_asleep = -1
most_sleepy_guard_id = -1

for key in elf_guards_data:
    if elf_guards_data[key].time_asleep > most_time_asleep:
        most_sleepy_guard_id = key
        most_time_asleep = elf_guards_data[key].time_asleep

print(f'Most sleepy guard is guard #{most_sleepy_guard_id} as he slept {most_time_asleep} minutes.')

# Initialize minutes during which elf was asleep
times_asleep_during_minute = dict()

for i in range(0, 60):
    times_asleep_during_minute[i] = 0


for key in sorted(times_and_events):

    if times_and_events[key].__contains__('#'):
        current_guard_id = int(times_and_events[key].split('#')[1].split(' ')[0])

    if current_guard_id != most_sleepy_guard_id:
        continue

    # print(f'{str(key)}: {times_and_events[key]}')

    if times_and_events[key].__contains__('falls'):
        sleep_start = key.minute

    if times_and_events[key].__contains__('wakes'):
        for i in range(sleep_start, key.minute):
            times_asleep_during_minute[i] += 1

minute_of_most_sleeps = -1
most_times_asleep_on_minute = -1

for i in range(0, 60):
    if times_asleep_during_minute[i] > most_times_asleep_on_minute:
        most_times_asleep_on_minute = times_asleep_during_minute[i]
        minute_of_most_sleeps = i

print(f'He slept most on minute {minute_of_most_sleeps}.')
print(f'Puzzle solution is thus equal to {most_sleepy_guard_id * minute_of_most_sleeps}.')
