#!python

from aoc2019.processor import Processor
from pathlib import Path
from typing import List, Tuple


def find_output(processor: Processor, value: int) -> int:
    for noun in range(100):
        for verb in range(100):
            if processor.prime(noun, verb).run()[0] == value:
                return 100 * noun + verb
    return -1


def main():
    script_path = Path.resolve(Path(__file__))
    with open(Path(script_path.parent, f"{script_path.stem}.txt"), "r") as input_data:
        input_data = input_data.readline().rstrip("\n")
        code = list(map(int, input_data.split(",")))
        processor = Processor(code)
        processor.prime(12, 2)
        print(f"Result code (12, 2): {processor.run()[0]}")
        value = 19690720
        result = find_output(processor, value)
        if result > 0:
            print(f"Result for {value}: {result}")
        else:
            raise Exception("Wrong value of code")


if __name__ == "__main__":
    main()
