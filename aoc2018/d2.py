from aoc.classes import AoCResult, AoCReturn
from typing import List


def main(puzzle_input: List[str]):
    for i, line in enumerate(puzzle_input):
        for j, cline in enumerate(puzzle_input):
            if i == j:
                continue
            diff = [i for i in range(len(line)) if line[i] != cline[i]]
            if len(diff) == 1:
                common = line[: diff[0]] + line[diff[0] + 1 :]
                return AoCReturn(
                    (AoCResult(None, ""), AoCResult(common, "Common characters found"))
                )


if __name__ == "__main__":
    raise Exception("Please use the run script")
