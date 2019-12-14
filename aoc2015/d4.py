from hashlib import md5
from typing import List

from aoc.classes import Result, ResultReturn


def main(puzzle_input: List[str]):

    input_val = puzzle_input[0]

    number = 0

    five = False
    six = False
    while True:
        hash = md5(bytes(f"{input_val}{number}".encode("utf-8"))).hexdigest()
        if hash.startswith("00000") and not five:
            result_1 = Result(number, "5 zero hash")
            five = True
        if hash.startswith("000000") and not six:
            result_2 = Result(number, "6 zero hash")
            six = True
        if five and six:
            break
        number += 1

    return ResultReturn((result_1, result_2))


if __name__ == "__main__":
    raise Exception("Please use the run script")
