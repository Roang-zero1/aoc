from aoc.classes import AoCResult, AoCReturn
from collections import defaultdict
from typing import List


def main(puzzle_input: List[str]):
    houses_1 = defaultdict(int)
    houses_2 = defaultdict(int)
    pos = {
        "c1": {"x": 0, "y": 0},
        "santa": {"x": 0, "y": 0},
        "robo_santa": {"x": 0, "y": 0},
    }
    houses_1[(0, 0)] += 1
    houses_2[(0, 0)] += 1
    for i, direction in enumerate(puzzle_input[0]):
        mover = "robo_santa" if i % 2 else "santa"
        if direction == "^":
            pos["c1"]["y"] -= 1
            pos[mover]["y"] -= 1
        elif direction == ">":
            pos["c1"]["x"] += 1
            pos[mover]["x"] += 1
        elif direction == "<":
            pos["c1"]["x"] -= 1
            pos[mover]["x"] -= 1
        elif direction == "v":
            pos["c1"]["y"] += 1
            pos[mover]["y"] += 1
        houses_1[(pos["c1"]["x"], pos["c1"]["y"])] += 1
        houses_2[(pos[mover]["x"], pos[mover]["y"])] += 1

    return AoCReturn(
        (
            AoCResult(len(houses_1), "Number of houses"),
            AoCResult(len(houses_2), "Robot delivery"),
        )
    )


if __name__ == "__main__":
    raise Exception("Please use the run script")
