#!python
from typing import Dict, List, Set, Tuple

from aoc.classes import Result, ResultReturn

DIRECTION_MAP = {"U": (0, 1), "D": (0, -1), "R": (1, 0), "L": (-1, 0)}


class WireTracer:

    wires: List[Set[Tuple[int, int]]]
    timings: List[Dict[Tuple[int, int], int]]

    def __init__(self, wire_1: List[str], wire_2: List[str]) -> None:
        self.wires = []
        self.timings = []
        self.run_wire(wire_1)
        self.run_wire(wire_2)

    def run_wire(self, wire: List[str]) -> None:
        wire_positions = []
        timings: Dict[Tuple[int, int], int] = {}
        position_x = 0
        position_y = 0
        timing = 0
        for direction in wire:
            direction_values = DIRECTION_MAP[direction[:1]]
            length = int(direction[1:])
            for _ in range(0, length):
                timing += 1
                position_x += direction_values[0]
                position_y += direction_values[1]
                position = (position_x, position_y)
                wire_positions.append((position))
                if position not in timings:
                    timings[position] = timing

        self.wires.append(set(wire_positions))
        self.timings.append(timings)

    def find_distance(self) -> int:
        intersections = self.wires[0].intersection(self.wires[1])
        distances = list(
            map(
                lambda intersection: abs(intersection[0]) + abs(intersection[1]),
                intersections,
            )
        )
        return min(distances)

    def find_timing(self) -> int:
        intersections = self.wires[0].intersection(self.wires[1])
        timings = list(
            map(
                lambda intersection: self.timings[0][intersection]
                + self.timings[1][intersection],
                intersections,
            )
        )
        return min(timings)


def main(puzzle_input: List[str]) -> ResultReturn:
    wires = []
    for line in puzzle_input:
        values = line.split(",")
        wires.append(values)
    tracer = WireTracer(wires[0], wires[1])
    return ResultReturn(
        (
            Result(tracer.find_distance(), "Wire distance"),
            Result(tracer.find_timing(), "Best timing"),
        )
    )


if __name__ == "__main__":
    raise Exception("Please use the run script")
