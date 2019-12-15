import logging
from typing import List

from aoc.classes import AoCResult, AoCReturn

logger = logging.getLogger(__name__)


def main(puzzle_input: List[str]):
    logger.debug("Input has %s lines", len(puzzle_input))

    # TODO: Implement solution #1
    result_1 = AoCResult(None, "NotYetImplemented")

    # TODO: Implement solution #2
    result_2 = AoCResult(None, "NotYetImplemented")

    return AoCReturn((result_1, result_2))


if __name__ == "__main__":
    raise Exception("Please use the run script")
