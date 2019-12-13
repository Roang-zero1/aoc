from typing import List, Tuple


class Processor:
    original_state: List[int]
    code: List[int]

    def __init__(self, code: List[int]) -> None:
        self.code = code
        self.original_state = code.copy()

    def run(self) -> List[int]:
        map = {1: self.add, 2: self.mul}
        cursor = 0
        while self.code[cursor] != 99:
            first = self.code[self.code[cursor + 1]]
            second = self.code[self.code[cursor + 2]]
            result = map[self.code[cursor]](first, second)
            self.code[self.code[cursor + 3]] = result[0]
            cursor += result[1]

        return self.code

    def prime(self, noun: int, verb: int) -> "Processor":
        self.reset()
        self.code[1] = noun
        self.code[2] = verb
        return self

    def reset(self) -> None:
        self.code = self.original_state.copy()

    def add(self, first: int, second: int) -> Tuple[int, int]:
        return (first + second, 4)

    def mul(self, first: int, second: int) -> Tuple[int, int]:
        return (first * second, 4)
