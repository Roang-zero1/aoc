#!python
import argparse
import importlib
from argparse import Namespace
from pathlib import Path
from typing import List

from tabulate import tabulate

from aoc.classes import AoCReturn
import logging


def main(args: Namespace):
    i = importlib.import_module(f"aoc{args.year}.d{args.day}")

    lines: List[str] = []
    base_path = Path.resolve(Path(__file__)).parent
    with open(
        Path(base_path, "input", f"aoc{args.year}", f"d{args.day}.txt"), "r"
    ) as input_data:
        for line in input_data.readlines():
            line = line.rstrip("\n")
            lines.append(line)
    result: AoCReturn = i.main(lines)  # type: ignore
    print(f"~~~ Advent of Code ~ {args.year} day {args.day}")
    print(
        tabulate(
            [
                ["Solution1", result.results[0].result, result.results[0].comment],
                ["Solution2", result.results[1].result, result.results[1].comment],
            ]
        )
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Calculate the solution to AoC riddles"
    )
    parser.add_argument(
        "year", metavar="Y", type=int, help="The year to search for the solution in"
    )
    parser.add_argument(
        "day", metavar="D", type=int, help="The day to search for the solution for"
    )
    parser.add_argument(
        "-v", "--verbose", help="increase output verbosity", action="store_true"
    )
    args = parser.parse_args()
    level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=level)
    main(args)
