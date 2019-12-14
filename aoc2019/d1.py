#!python
from typing import List, Tuple

from aoc.classes import Result, ResultReturn


def calculate_fuel(mass: int) -> Tuple[int, int]:
    sum: int = 0
    result = int(mass / 3) - 2
    if result > 0:
        sum += result
        sum += calculate_fuel(result)[1]

    return (result, sum)


def calculate_total_fuel(masses: List[int]) -> Tuple[int, int]:
    sum = 0
    sum_with_fuel = 0
    for mass in masses:
        result = calculate_fuel(mass)
        sum += result[0]
        sum_with_fuel += result[1]
    return (sum, sum_with_fuel)


def main(puzzle_input: List[str]) -> ResultReturn:
    masses = []
    for line in puzzle_input:
        masses.append(int(line))

    sum, sum_with_fuel = calculate_total_fuel(masses)

    return ResultReturn(
        (Result(sum, "Required fuel"), Result(sum_with_fuel, "Required fuel with fuel"))
    )


if __name__ == "__main__":
    raise Exception("Please use the run script")
