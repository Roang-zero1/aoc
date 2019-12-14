from typing import List

from aoc.classes import Result, ResultReturn


def main(puzzle_input: List[str]):
    sum_escaped = 0
    sum_decoded = 0
    sum_double_encoded = 0
    for line in puzzle_input:
        o_line = line
        sum_escaped += len(line)
        line = line[1:-1]
        line = bytes(line, "utf-8").decode("unicode_escape")
        sum_decoded += len(line)
        line = o_line
        line = line.replace('"', '\\"')
        line = line.replace("\\", "\\\\")
        line = line.replace('\\"', '"')
        sum_double_encoded += len(line) + 2

    return ResultReturn(
        (
            Result(sum_escaped - sum_decoded, "Difference escaped/decoded"),
            Result(
                sum_double_encoded - sum_escaped, "Difference escaped/double escaped"
            ),
        )
    )


if __name__ == "__main__":
    raise Exception("Please use the run script")
