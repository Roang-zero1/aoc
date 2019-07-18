from collections import defaultdict, Counter
from dataclasses import dataclass
from typing import List, Dict, Union
from enum import Enum


class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


MIN_SIZE = 0
MAX_SIZE = 0
MAX_SAFE_DISTANCE = 10000

DIRECTIONS = [Direction.UP, Direction.RIGHT, Direction.DOWN, Direction.LEFT]


@dataclass
class Point:
    ident: int
    x: int
    y: int
    infinite: bool
    finished: bool

    def __hash__(self):
        return hash((self.ident, self.x, self.y))


@dataclass
class GridPoint:
    distances: dict
    safe_distance: bool = False
    origin: Union[None, Point] = None


GRID_TYPE = List[List[GridPoint]]


def print_grid(grid: GRID_TYPE):

    print(f'  | {" | ".join([f"{x:02d}" for x in range(MAX_SIZE+1)])} |')
    print(f'  |-{"-----" * MAX_SIZE}---|')
    row_count = 0
    for row in grid:
        print(f"{row_count:02d}|", end="")
        for line in row:
            if line.origin:
                print(f">{line.origin.ident:02d}<", end="")
            elif line.safe_distance:
                print(" ## ", end="")
            elif line.distances:
                max_distance = max(line.distances)
                if len(line.distances[max_distance]) > 1:
                    print(" :: ", end="")
                else:
                    point = list(line.distances[max_distance])[0]
                    print(f" {point.ident:02d} ", end="")
            else:
                print(" .. ", end="")
            print("|", end="")
        row_count += 1
        print("\n", end="")


DIRMULTIPLIER = {
    Direction.UP: {"main": "y", "off": "x", "mmulti": -1},
    Direction.RIGHT: {"main": "x", "off": "y", "mmulti": 1},
    Direction.DOWN: {"main": "y", "off": "x", "mmulti": 1},
    Direction.LEFT: {"main": "x", "off": "y", "mmulti": -1},
}


def add_point_to_grid(
    grid: GRID_TYPE,
    x: int,
    y: int,
    point: Point,
    distance: int,
    points_in_progress: set,
) -> None:
    if x < MIN_SIZE or x > MAX_SIZE or y < MIN_SIZE or y > MAX_SIZE:
        return

    if grid[y][x].distances:
        max_distance = max(grid[y][x].distances)
        if distance > max_distance:
            return

    if grid[y][x].origin:
        return

    grid[y][x].distances[distance].add(point)
    points_in_progress.add(point)


def manhattan_distancer(
    grid: GRID_TYPE,
    point: Point,
    direction: Direction,
    distance: int,
    points_in_progress: set,
) -> None:
    for x in range(distance):
        main_offset = (distance - x) * DIRMULTIPLIER[direction]["mmulti"]

        if DIRMULTIPLIER[direction]["main"] == "x":
            main_position = (
                getattr(point, DIRMULTIPLIER[direction]["main"]) + main_offset
            )
            off_position_neg = getattr(point, DIRMULTIPLIER[direction]["off"]) - x
            off_position_pos = getattr(point, DIRMULTIPLIER[direction]["off"]) + x

            add_point_to_grid(
                grid,
                main_position,
                off_position_neg,
                point,
                distance,
                points_in_progress,
            )
            add_point_to_grid(
                grid,
                main_position,
                off_position_pos,
                point,
                distance,
                points_in_progress,
            )
        else:
            main_position = (
                getattr(point, DIRMULTIPLIER[direction]["main"]) + main_offset
            )
            off_position_neg = getattr(point, DIRMULTIPLIER[direction]["off"]) - x
            off_position_pos = getattr(point, DIRMULTIPLIER[direction]["off"]) + x

            add_point_to_grid(
                grid,
                off_position_neg,
                main_position,
                point,
                distance,
                points_in_progress,
            )
            add_point_to_grid(
                grid,
                off_position_pos,
                main_position,
                point,
                distance,
                points_in_progress,
            )


def expand(
    grid: GRID_TYPE, points: Dict[int, Point], distance: int, points_in_progress: set
) -> None:
    for point in [v for v in points.values() if not v.finished]:
        for direction in DIRECTIONS:
            manhattan_distancer(grid, point, direction, distance, points_in_progress)

def part1(points: Dict[int, Point]):
    grid = [
        [GridPoint(defaultdict(set)) for x in range(MAX_SIZE + 1)]
        for y in range(MAX_SIZE + 1)
    ]

    for point in points.values():
        grid[point.y][point.x].origin = point

    for distance in range(1, MAX_SIZE):
        points_in_progress = set()
        expand(grid, points, distance, points_in_progress)
        if not points_in_progress:
            break

    for y in range(MIN_SIZE, MAX_SIZE):
        for x in [MIN_SIZE, MAX_SIZE]:
            max_distance = max(grid[y][x].distances, default=-1)
            if max_distance > 0 and len(grid[y][x].distances[max_distance]) == 1:
                list(grid[y][x].distances[max_distance])[0].infinite = True

    for y in [MIN_SIZE, MAX_SIZE]:
        for x in range(MIN_SIZE, MAX_SIZE):
            max_distance = max(grid[y][x].distances, default=-1)
            if max_distance > 0 and len(grid[y][x].distances[max_distance]) == 1:
                list(grid[y][x].distances[max_distance])[0].infinite = True

    count_points = []

    for y in range(MIN_SIZE, MAX_SIZE):
        for x in range(MIN_SIZE, MAX_SIZE):
            if grid[y][x].origin:
                count_points.append(grid[y][x].origin)
            max_distance = max(grid[y][x].distances, default=-1)
            if max_distance > 0 and len(grid[y][x].distances[max_distance]) == 1:
                if not list(grid[y][x].distances[max_distance])[0].infinite:
                    count_points.append(list(grid[y][x].distances[max_distance])[0])

    counts = Counter(
        [
            max_distance
            for max_distance in count_points
            if max_distance.infinite == False
        ]
    )

    # print(counts)

    # print_grid(grid)

    print(f"Solution is: {max(counts.values())}")

def part2(points: Dict[int, Point]):
    grid = [
        [GridPoint(defaultdict(set)) for x in range(MAX_SIZE + 1)]
        for y in range(MAX_SIZE + 1)
    ]

    for point in points.values():
        grid[point.y][point.x].origin = point

    for y in range(MIN_SIZE, MAX_SIZE):
        for x in range(MIN_SIZE, MAX_SIZE):
            total_distance = 0
            for point in points.values():
                total_distance += abs(point.y - y) + abs(point.x -x)
            if total_distance < MAX_SAFE_DISTANCE:
                grid_point =  grid[y][x]
                grid_point.safe_distance = True
                grid[y][x] = grid_point

    region_size = 0
    for y in range(MIN_SIZE, MAX_SIZE):
        for x in range(MIN_SIZE, MAX_SIZE):
            if grid[y][x].safe_distance == True:
                region_size += 1

    #print_grid(grid)

    print(region_size)


def main():
    global MAX_SIZE

    points = {}
    with open("d6.txt", "r") as input_data:
        lines = input_data.readlines()
        ident = 1
        for line in lines:
            line = line.rstrip("\n")
            point_data = line.split(", ")
            point = Point(ident, int(point_data[0]), int(point_data[1]), False, False)
            points[ident] = point
            ident = ident + 1
            if point.y > MAX_SIZE:
                MAX_SIZE = point.y + 1
            if point.x > MAX_SIZE:
                MAX_SIZE = point.x + 1

    #part1(points)
    part2(points)


if __name__ == "__main__":
    main()
