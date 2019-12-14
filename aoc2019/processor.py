from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Union

PARAMETER_COUNT = 2


class ResultMode(Enum):
    INPUT = 0
    OUTPUT = 1
    FINISHED = 2
    CONTINUE = 3


class ParameterMode(Enum):
    POSITION = 0
    IMMEDIATE = 1


@dataclass
class Instruction:
    cursor: int
    op_code: int = 99
    result: ResultMode = ResultMode.CONTINUE


class Processor:
    original_state: List[int]
    code: List[int]
    instruction: Instruction
    parameters: Dict[int, Union[int, None]]
    parameter_modes: Dict[int, ParameterMode]

    def __init__(self, code: List[int]) -> None:
        self.code = code
        self.instruction = Instruction(0)
        self.original_state = code.copy()
        self.parameters = {}
        self.parameter_modes = {}
        for parameter in range(PARAMETER_COUNT):
            self.parameters[parameter] = None
            self.parameter_modes[parameter] = ParameterMode.POSITION

    def parse_opcode(self) -> None:
        cursor = self.instruction.cursor
        opcode = self.code[cursor] % 100
        modes = self.code[cursor] // 100
        for parameter in range(PARAMETER_COUNT):
            self.parameter_modes[parameter] = ParameterMode(modes % 10)
            modes = modes // 10
        self.instruction = Instruction(self.instruction.cursor, opcode)

    def read_parameters(self, parameter_count: int):
        self.parameters = dict.fromkeys(self.parameters, None)
        for parameter in range(parameter_count):
            self.parameters[parameter] = (
                self.code[self.code[self.instruction.cursor + 1 + parameter]]
                if self.parameter_modes[parameter] == ParameterMode.POSITION
                else self.code[self.instruction.cursor + 1 + parameter]
            )

    def run(self) -> List[int]:
        self.instruction = Instruction(0)
        return self.continue_operation()

    def continue_operation(self) -> List[int]:
        function_map = {
            1: self.add,
            2: self.mul,
            3: self.save,
            4: self.read,
            99: self.finish,
        }
        while self.instruction.result == ResultMode.CONTINUE:
            self.parse_opcode()
            function_map[self.instruction.op_code]()

        return self.code

    def prime(self, noun: int, verb: int) -> "Processor":
        self.reset()
        self.code[1] = noun
        self.code[2] = verb
        return self

    def reset(self) -> None:
        self.code = self.original_state.copy()

    def add(self) -> None:
        self.read_parameters(2)
        if self.parameters[0] is None or self.parameters[1] is None:
            raise ValueError("Invalid value for addition given")
        self.code[self.code[self.instruction.cursor + 3]] = (
            self.parameters[0] + self.parameters[1]
        )
        self.instruction = Instruction(self.instruction.cursor + 4)

    def mul(self) -> None:
        self.read_parameters(2)
        if self.parameters[0] is None or self.parameters[1] is None:
            raise ValueError("Invalid value for addition given")
        self.code[self.code[self.instruction.cursor + 3]] = (
            self.parameters[0] * self.parameters[1]
        )
        self.instruction = Instruction(self.instruction.cursor + 4)

    def finish(self):
        self.instruction = Instruction(0, result=ResultMode.FINISHED)

