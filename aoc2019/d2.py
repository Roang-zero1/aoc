#!python

from typing import List

from aoc2019.processor import Processor
from aoc.classes import AoCResult, AoCReturn


def find_output(processor: Processor, value: int) -> int:
    for noun in range(100):
        for verb in range(100):
            if processor.prime(noun, verb).run()[1][0] == value:
                return 100 * noun + verb
    return -1


def main(puzzle_input: List[str]) -> AoCReturn:
    code = list(map(int, puzzle_input[0].split(",")))
    processor = Processor(code)
    processor.prime(12, 2)
    result_1 = AoCResult(processor.run()[1][0], "Result code (12, 2)")
    value = 19690720
    result = find_output(processor, value)
    if result > 0:
        return AoCReturn((result_1, AoCResult(result, f"Result for {value}")))
    else:
        raise Exception("Wrong value of code")


if __name__ == "__main__":
    raise Exception("Please use the run script")
