from aoc.classes import Result, ResultReturn
from typing import List


vowels = ["a", "e", "i", "o", "u"]
naughty = ["ab", "cd", "pq", "xy"]


def main(puzzle_input: List[str]):

    nice = 0
    for line in puzzle_input:
        contains_naughty = any(x in line for x in naughty)
        double = False
        prev_char = ""
        v_count = 0
        for char in line:
            if char in vowels:
                v_count += 1
            if prev_char == char:
                double = True
            elif double == False:
                prev_char = char
            if double and v_count >= 3:
                break
        if v_count >= 3 and not contains_naughty and double:
            nice += 1

    result_1 = Result(nice, "Sum of nice strings")

    nice = 0
    for line in puzzle_input:
        double = False
        double_pairs = False
        for i in range(len(line) - 2):
            if line[i] == line[i + 2]:
                double = True
            if line.count(f"{line[i]}{line[i+1]}") > 1:
                double_pairs = True
        if double and double_pairs:
            nice += 1

    result_2 = Result(nice, "Sum of nice strings")
    return ResultReturn((result_1, result_2))


if __name__ == "__main__":
    raise Exception("Please use the run script")
