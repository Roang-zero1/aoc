import logging
from collections import defaultdict
from typing import DefaultDict, Dict, List

from aoc.classes import Result, ResultReturn

logger = logging.getLogger(__name__)


def main(puzzle_input: List[str]):
    entries: DefaultDict[str, DefaultDict[str, str]] = defaultdict(
        lambda: defaultdict(str)
    )
    for line in puzzle_input:
        words = line.split()
        date = words[0].lstrip("[")
        time = words[1].rstrip("]")
        entries[date][time] = words[3]

    s_dates = sorted(entries.keys())
    guard_id = 0
    guards: DefaultDict[int, DefaultDict[str, DefaultDict[int, bool]]] = defaultdict(
        lambda: defaultdict(lambda: defaultdict(bool))
    )
    for date in s_dates:
        s_times = sorted(entries[date].keys())
        for time in s_times:
            minute = int(time.split(":")[1])
            val = entries[date][time].lstrip("#")
            if val.isdigit():
                # print(f'Guard {val} begins shift')
                guard_id = int(val)
            else:
                # print(f'Guard {guard_id} {val}')
                guards[guard_id][date][minute] = val == "asleep"

    guard_times = {}
    for guard, dates in guards.items():
        logger.debug("Analyzing guard: %s", guard)
        guard_times[guard] = {"minutes": defaultdict(int), "asleep": 0, "asleep_len": 0}
        for times in dates.values():
            day_times = []
            for time in sorted(times):
                day_times.append(time)
            for i in range(0, len(day_times), 2):
                for t in range(day_times[i], day_times[i + 1]):
                    guard_times[guard]["minutes"][t] += 1
                    guard_times[guard]["asleep"] += 1

    result = 0
    max_minutes = 0
    worst_guard = 0
    worst_minute = None
    worst_guard_2 = 0
    worst_minute_2 = 0
    worst_minute_2_val = 0
    for guard, values in guard_times.items():
        asleep = values["asleep"]
        minutes = values["minutes"]
        if asleep > max_minutes:
            max_minutes = asleep
            worst_guard = guard
            worst_minute_g = None
            for minute in sorted(minutes.keys()):
                if worst_minute_g:
                    worst_minute_g = (
                        minute
                        if minutes[worst_minute_g] < minutes[minute]
                        else worst_minute_g
                    )
                else:
                    worst_minute_g = minute
            worst_minute = worst_minute_g
        for minute in sorted(minutes.keys()):
            if minutes[minute] > worst_minute_2_val:
                worst_guard_2 = guard
                worst_minute_2 = minute
                worst_minute_2_val = minutes[minute]

    logging.debug(
        "Guard %s is asleep for %s minutes, he is at his worst at %s",
        worst_guard,
        max_minutes,
        worst_minute,
    )

    logging.debug(
        "Guard %s is asleep %s times in minute %s",
        worst_guard_2,
        guard_times[worst_guard_2]["minutes"][worst_minute_2],
        worst_minute_2,
    )
    return ResultReturn(
        (
            Result(worst_guard * worst_minute, "Worst guard for sleeping"),
            Result(worst_guard_2 * worst_minute_2, "Worst gurard in most minutes"),
        )
    )


if __name__ == "__main__":
    raise Exception("Please use the run script")
