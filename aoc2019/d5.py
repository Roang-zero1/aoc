#!python

from aoc.classes import AoCResult, AoCReturn
from typing import List

from aoc2019.processor import Processor, ResultMode

import logging

logger = logging.getLogger(__name__)


def main(input: List[str]):
    code = list(map(int, input[0].split(",")))
    processor = Processor(code)
    result = processor.run()
    if result[0] != ResultMode.INPUT:
        raise Exception("Unexpected result, verify input")

    result = processor.continue_operation(1)
    diagnostic_code = -1
    while True:
        if result[0] == ResultMode.OUTPUT:
            diagnostic_code = result[1]
            logger.debug("Status of operation %s", result[1])
        elif result[0] == ResultMode.FINISHED:
            break
        result = processor.continue_operation()

    if diagnostic_code == -1:
        raise Exception("Failed to obtain diagnostic code")

    result_1 = AoCResult(diagnostic_code, "diagnostic code - air conditioner unit")

    processor.reset()
    result = processor.run()
    if result[0] != ResultMode.INPUT:
        raise Exception("Unexpected result, verify input")
    result = processor.continue_operation(5)
    diagnostic_code = result[1]
    processor.continue_operation()

    result_2 = AoCResult(
        diagnostic_code, "diagnostic code - thermal radiator controller"
    )

    return AoCReturn((result_1, result_2))


if __name__ == "__main__":
    raise Exception("Please use the run script")
