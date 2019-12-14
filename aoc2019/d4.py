from aoc.classes import AoCResult, AoCReturn
from typing import List


def test_password(password: int, strict_double: bool = False):
    password_string = str(password)
    double = False
    for i in range(5):
        number = int(password_string[i])
        next = int(password_string[i + 1])
        if number == next:
            if strict_double:
                count = 2
                if i - 1 >= 0 and number == int(password_string[i - 1]):
                    count += 1
                if i + 2 < 6 and number == int(password_string[i + 2]):
                    count += 1
                if count == 2:
                    double = True
            else:
                double = True

        if next < number:
            return False
    if double:
        return True
    return False


def main(puzzle_input: List[str]) -> AoCReturn:
    input_values = list(map(int, puzzle_input[0].split("-")))
    sum_valid = 0
    sum_valid_strict = 0
    for password in range(input_values[0], input_values[1] + 1):
        if test_password(password):
            sum_valid += 1
            if test_password(password, True):
                sum_valid_strict += 1
    return AoCReturn(
        (
            AoCResult(sum_valid, "Sum valid passwords"),
            AoCResult(sum_valid_strict, "Sum of valid passwords with additional checks"),
        )
    )


if __name__ == "__main__":
    raise Exception("Please use the run script")
