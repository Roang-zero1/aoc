from typing import List

from aoc.classes import Result, ResultReturn


def main(puzzle_input: List[str]):
    floor = 0
    basement = False
    for line in puzzle_input:
        for i, char in enumerate(line):
            if char == "(":
                floor += 1
            elif char == ")":
                floor -= 1
            if floor == -1 and not basement:
                result_2 = Result(i + 1, "Basement entered")
                basement = True
    result_1 = Result(floor, "Final floor")
    return ResultReturn((result_1, result_2))


if __name__ == "__main__":
    raise Exception("Please use the run script")
