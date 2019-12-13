#!python
from pathlib import Path
from typing import Tuple, List


def calculate_fuel(mass: int) -> Tuple[int, int]:
    sum: int = 0
    result = int(mass / 3) - 2
    if result > 0:
        sum += result
        sum += calculate_fuel(result)[1]

    return (result, sum)


def calculate_total_fuel(masses: List[int]) -> Tuple[int, int]:
    sum = 0
    sum_with_fuel = 0
    for mass in masses:
        result = calculate_fuel(mass)
        sum += result[0]
        sum_with_fuel += result[1]
    return (sum, sum_with_fuel)


def main():
    script_path = Path.resolve(Path(__file__))
    masses = []
    with open(Path(script_path.parent, f"{script_path.stem}.txt"), "r") as input_data:
        lines = input_data.readlines()
        for line in lines:
            line = line.rstrip("\n")
            masses.append(int(line))

    sum, sum_with_fuel = calculate_total_fuel(masses)

    print(f"Required fuel sum is : {sum}")
    print(f"Required fuel sum,  with fuel for fuel, is : {sum_with_fuel}")


if __name__ == "__main__":
    main()
