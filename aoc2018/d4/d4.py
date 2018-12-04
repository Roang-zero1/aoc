import pprint

from collections import defaultdict
entries = defaultdict(lambda: defaultdict(str))
with open('input.txt') as input_file:
    for line in input_file.readlines():
        words = line.split()
        date = words[0].lstrip('[')
        time = words[1].rstrip(']')
        entries[date][time] = words[3]
s_dates = sorted(entries.keys())
guard_id = 0
guards = defaultdict(lambda: defaultdict(lambda: defaultdict(bool)))
for date in s_dates:
    s_times = sorted(entries[date].keys())
    for time in s_times:
        minute = int(time.split(':')[1])
        val = entries[date][time].lstrip('#')
        if val.isdigit():
            #print(f'Guard {val} begins shift')
            guard_id = int(val)
        else:
            #print(f'Guard {guard_id} {val}')
            guards[guard_id][date][minute] = val == "asleep"

guard_times = {}
for guard,dates in guards.items():
    #print(f"Analysing guard: {guard}")
    guard_times[guard] = {
        'minutes': defaultdict(int),
        'asleep': 0,
        'asleep_len': 0
    }
    for times in dates.values():
        day_times = []
        for time in sorted(times):
            day_times.append(time)
        for i in range(0, len(day_times), 2):
            for t in range(day_times[i], day_times[i+1] ):
                guard_times[guard]['minutes'][t] += 1
                guard_times[guard]['asleep'] += 1

result = 0
max_minutes = 0
worst_guard = 0
worst_minute = None
worst_guard_2 = 0
worst_minute_2 = 0
worst_minute_2_val = 0
for guard, values in guard_times.items():
    asleep = values['asleep']
    minutes = values['minutes']
    if asleep > max_minutes:
        max_minutes = asleep
        worst_guard = guard
        worst_minute_g = None
        for minute in sorted(minutes.keys()):
            if worst_minute_g:
                worst_minute_g = minute if minutes[worst_minute_g] < minutes[minute] else worst_minute_g
            else:
                worst_minute_g = minute
        worst_minute = worst_minute_g
    for minute in sorted(minutes.keys()):
        if minutes[minute] > worst_minute_2_val:
            worst_guard_2 = guard
            worst_minute_2 = minute
            worst_minute_2_val = minutes[minute]

print(f'Guard {worst_guard} is asleep for {max_minutes} minutes, he is at his worst at {worst_minute}')
print(f'solution {worst_guard * worst_minute}')

print(f'Guard {worst_guard_2} is asleep {guard_times[worst_guard_2]["minutes"][worst_minute_2]} '
f'times in minute {worst_minute_2}')
print(f'solution {worst_guard_2 * worst_minute_2}')