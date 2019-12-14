from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Union

PARAMETER_COUNT = 2


@dataclass
class Instruction:
    Cursor: int
    OPCode: int


class ParameterMode(Enum):
    POSITION = 0
    IMMEDIATE = 1


class Processor:
    original_state: List[int]
    code: List[int]
    parameters: Dict[int, Union[int, None]]
    parameter_modes: Dict[int, ParameterMode]

    def __init__(self, code: List[int]) -> None:
        self.code = code
        self.original_state = code.copy()
        self.parameters = {}
        self.parameter_modes = {}
        for parameter in range(PARAMETER_COUNT):
            self.parameters[parameter] = None
            self.parameter_modes[parameter] = ParameterMode.POSITION

    def parse_opcode(self, cursor: int) -> Instruction:
        opcode = self.code[cursor] % 100
        modes = self.code[cursor] // 100
        for parameter in range(PARAMETER_COUNT):
            self.parameter_modes[parameter] = ParameterMode(modes % 10)
            modes = modes // 10
        return Instruction(cursor, opcode)

    def read_parameters(self, inst: Instruction, parameter_count: int):
        self.parameters = dict.fromkeys(self.parameters, None)
        for parameter in range(parameter_count):
            self.parameters[parameter] = (
                self.code[self.code[inst.Cursor + 1 + parameter]]
                if self.parameter_modes[parameter] == ParameterMode.POSITION
                else self.code[inst.Cursor + 1 + parameter]
            )

    def run(self) -> List[int]:
        function_map = {
            1: self.add,
            2: self.mul,
            3: self.save,
            4: self.read,
        }
        cursor = 0
        while self.code[cursor] != 99:
            instruction = self.parse_opcode(cursor)
            cursor = function_map[instruction.OPCode](instruction)

        return self.code

    def prime(self, noun: int, verb: int) -> "Processor":
        self.reset()
        self.code[1] = noun
        self.code[2] = verb
        return self

    def reset(self) -> None:
        self.code = self.original_state.copy()

    def add(self, inst: Instruction) -> int:
        self.read_parameters(inst, 2)
        if self.parameters[0] is None or self.parameters[1] is None:
            raise ValueError("Invalid value for addition given")
        self.code[self.code[inst.Cursor + 3]] = self.parameters[0] + self.parameters[1]
        return inst.Cursor + 4

    def mul(self, inst: Instruction) -> int:
        self.read_parameters(inst, 2)
        if self.parameters[0] is None or self.parameters[1] is None:
            raise ValueError("Invalid value for addition given")
        self.code[self.code[inst.Cursor + 3]] = self.parameters[0] * self.parameters[1]
        return inst.Cursor + 4
