#!python
import logging
from typing import List, Set, Tuple

from aoc.classes import Result, ResultReturn

LOGGER = logging.getLogger(__name__)


def main(puzzle_input: List[str]) -> ResultReturn:
    changes = []
    for line in puzzle_input:
        changes.append(int(line))
    result_1 = Result(sum(changes), "Final position")
    loop_cnt = 0
    position = 0
    positions: Set[int] = set()
    found = False
    while loop_cnt < 3000 and not found:
        for change in changes:
            position += change
            if position in positions:
                found = True
                break
            else:
                positions.add(position)

        loop_cnt += 1
        LOGGER.debug(
            "loop %s checked %s positions current %s",
            loop_cnt,
            len(positions),
            position,
        )
    return ResultReturn((result_1, Result(position, "Final position")))


if __name__ == "__main__":
    raise Exception("Please use the run script")
