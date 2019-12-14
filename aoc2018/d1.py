#!python
import logging
from typing import List, Set, Tuple

from aoc.classes import AoCResult, AoCReturn

LOGGER = logging.getLogger(__name__)


def main(puzzle_input: List[str]) -> AoCReturn:
    changes = []
    for line in puzzle_input:
        changes.append(int(line))
    result_1 = AoCResult(sum(changes), "Final position")
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
    return AoCReturn((result_1, AoCResult(position, "Final position")))


if __name__ == "__main__":
    raise Exception("Please use the run script")
