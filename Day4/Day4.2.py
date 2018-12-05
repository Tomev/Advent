from datetime import datetime
from Day4.ElfGuard import ElfGuard

file_read = open("input.txt", "r")

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

    if times_and_events[key].__contains__('#'):
        current_guard_id = int(times_and_events[key].split('#')[1].split(' ')[0])
        sleep_start = 0

        if not elf_guards_data.__contains__(current_guard_id):
            elf_guards_data[current_guard_id] = ElfGuard(current_guard_id)

    if times_and_events[key].__contains__('falls'):
        sleep_start = key.minute

    if times_and_events[key].__contains__('wakes'):
        elf_guards_data[current_guard_id].time_asleep += key.minute - sleep_start

# Initialize minutes during which each elf was asleep
guard_times_asleep_during_minute = dict()

for guard_id in elf_guards_data:
    guard_times_asleep_during_minute[guard_id] = dict()

    for i in range(0, 60):
        guard_times_asleep_during_minute[guard_id][i] = 0


for key in sorted(times_and_events):

    if times_and_events[key].__contains__('#'):
        current_guard_id = int(times_and_events[key].split('#')[1].split(' ')[0])

    print(f'{str(key)}: {times_and_events[key]}')

    if times_and_events[key].__contains__('falls'):
        sleep_start = key.minute

    if times_and_events[key].__contains__('wakes'):
        for i in range(sleep_start, key.minute):
            guard_times_asleep_during_minute[current_guard_id][i] += 1

id_of_guard_most_frequently_asleep_on_given_minute = -1
minute_guard_sleeps_most_frequently_on = -1
max_frequency_of_sleeps = -1

for guard_id in elf_guards_data:
    for i in range(0, 60):
        if guard_times_asleep_during_minute[guard_id][i] > max_frequency_of_sleeps:
            max_frequency_of_sleeps = guard_times_asleep_during_minute[guard_id][i]
            minute_guard_sleeps_most_frequently_on = i
            id_of_guard_most_frequently_asleep_on_given_minute = guard_id

print(f'Guard #{id_of_guard_most_frequently_asleep_on_given_minute} sleeps most frequently ({max_frequency_of_sleeps} \
times) on same minute ({minute_guard_sleeps_most_frequently_on}).')
print(f'The solution to the puzzle is thus equal to {id_of_guard_most_frequently_asleep_on_given_minute * minute_guard_sleeps_most_frequently_on}.')
