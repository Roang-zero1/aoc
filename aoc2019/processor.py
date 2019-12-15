from aoc2019.processor_logger import get_processor_logger
from dataclasses import dataclass
from enum import Enum
from typing import Any, Dict, List, Tuple, Union

logger = get_processor_logger(__name__)

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
        logger.debug("Initializing processor", extra={"function": "__init__"})
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
        logger.debug("Parsing opcode %s", self.code[cursor])
        opcode = self.code[cursor] % 100
        modes = self.code[cursor] // 100
        for parameter in range(PARAMETER_COUNT):
            self.parameter_modes[parameter] = ParameterMode(modes % 10)
            modes = modes // 10
        self.instruction = Instruction(self.instruction.cursor, opcode)

    def read_parameters(self, parameter_count: int):
        logger.debug("Reading %s parameters", parameter_count)
        self.parameters = dict.fromkeys(self.parameters, None)
        for parameter in range(parameter_count):
            self.parameters[parameter] = (
                self.read(1 + parameter)
                if self.parameter_modes[parameter] == ParameterMode.POSITION
                else self.code[self.instruction.cursor + 1 + parameter]
            )
            logger.debug(
                "Parameter %i read as %i", parameter, self.parameters[parameter]
            )

    def run(self) -> Tuple[ResultMode, Any]:
        logger.debug("Starting run of current code at 0")
        self.instruction = Instruction(0)
        return self.continue_operation()

    def continue_operation(
        self, input: Union[int, None] = None
    ) -> Tuple[ResultMode, Any]:
        logger.debug(
            "Continuing operation at %s with from mode %s",
            self.instruction.cursor,
            self.instruction.result,
        )
        function_map = {
            1: self.add,
            2: self.mul,
            3: self.input,
            4: self.output,
            5: self.jump_if_true,
            6: self.jump_if_false,
            7: self.less_than,
            8: self.equals,
            99: self.finish,
        }
        retval = None

        if input is not None:
            self.input(input)
        else:
            self.instruction = Instruction(self.instruction.cursor)

        while self.instruction.result == ResultMode.CONTINUE:
            self.parse_opcode()
            if self.instruction.op_code not in function_map:
                raise Exception("Invalid operation")
            retval = function_map[self.instruction.op_code]()

        logger.debug(
            "Operation finished with result %s and return value %s",
            self.instruction.result,
            "<<code>>" if self.instruction.result == ResultMode.FINISHED else retval,
        )

        return (
            self.instruction.result,
            self.code if self.instruction.result == ResultMode.FINISHED else retval,
        )

    def prime(self, noun: int, verb: int) -> "Processor":
        logger.debug("Processor primed with noun '%s' and verb '%s'", noun, verb)
        self.reset()
        self.code[1] = noun
        self.code[2] = verb
        return self

    def reset(self) -> None:
        logger.debug("Processor reset")
        self.code = self.original_state.copy()

    def save(self, value: int, offset: int = 1):
        logger.debug("Value %s saved to %s", value, self.instruction.cursor + offset)
        self.code[self.code[self.instruction.cursor + offset]] = value

    def read(self, offset: int = 1) -> int:
        if self.instruction.cursor + offset > len(self.code):
            logger.error(
                "Index %s larger than code length %s",
                self.instruction.cursor + offset,
                len(self.code),
            )
            raise IndexError
        value = self.code[self.code[self.instruction.cursor + offset]]
        logger.debug("Value %s read from %s", value, self.instruction.cursor + offset)
        return value

    def input(self, value: Union[int, None] = None) -> None:
        if value is None:
            logger.debug("Requesting input")
            self.instruction = Instruction(
                self.instruction.cursor, result=ResultMode.INPUT
            )
        else:
            logger.debug("Processing input: %s", value)
            self.save(value)
            self.instruction = Instruction(self.instruction.cursor + 2)

    def output(self) -> int:
        logger.debug("Output value from: %s", self.instruction.cursor + 1)
        self.read_parameters(1)
        value = self.parameters[0]
        if value is None:
            raise ValueError("Invalid value read")
        self.instruction = Instruction(
            self.instruction.cursor + 2, result=ResultMode.OUTPUT
        )
        return value

    def add(self) -> None:
        logger.debug("Adding values")
        self.read_parameters(2)
        if self.parameters[0] is None or self.parameters[1] is None:
            raise ValueError("Invalid value for addition given")
        self.save(self.parameters[0] + self.parameters[1], 3)
        self.instruction = Instruction(self.instruction.cursor + 4)

    def mul(self) -> None:
        logger.debug("Multiplying values")
        self.read_parameters(2)
        if self.parameters[0] is None or self.parameters[1] is None:
            raise ValueError("Invalid value for addition given")
        self.save(self.parameters[0] * self.parameters[1], 3)
        self.instruction = Instruction(self.instruction.cursor + 4)

    def jump_if_true(self) -> None:
        self.read_parameters(2)
        if self.parameters[0] != 0:
            address = self.parameters[1]
            if address:
                logger.debug("Jump to address %s", address)
                self.instruction = Instruction(address)
            else:
                raise ValueError("Invalid jump address found")
        else:
            logger.debug("Do not jump")
            self.instruction = Instruction(self.instruction.cursor + 3)

    def jump_if_false(self) -> None:
        self.read_parameters(2)
        if self.parameters[0] == 0:
            address = self.parameters[1]
            if address:
                logger.debug("Jump to address %s", address)
                self.instruction = Instruction(address)
            else:
                raise ValueError("Invalid jump address found")
        else:
            logger.debug("Do not jump")
            self.instruction = Instruction(self.instruction.cursor + 3)

    def less_than(self) -> None:
        self.read_parameters(2)
        parameter_1 = self.parameters[0]
        parameter_2 = self.parameters[1]
        logger.debug("Check less than for %s < %s", parameter_1, parameter_2)
        if parameter_1 and parameter_2:
            if parameter_1 < parameter_2:
                self.save(1, 3)
            else:
                self.save(0, 3)
            self.instruction = Instruction(self.instruction.cursor + 4)
        else:
            raise ValueError("Invalid parameters found")

    def equals(self) -> None:
        self.read_parameters(2)
        parameter_1 = self.parameters[0]
        parameter_2 = self.parameters[1]
        logger.debug("Check equal for %s and %s", parameter_1, parameter_2)
        if parameter_1 and parameter_2:
            if parameter_1 == parameter_2:
                self.save(1, 3)
            else:
                self.save(0, 3)
            self.instruction = Instruction(self.instruction.cursor + 4)
        else:
            raise ValueError("Invalid parameters found")

    def finish(self):
        logger.debug("Finishing execution")
        self.instruction = Instruction(0, result=ResultMode.FINISHED)
