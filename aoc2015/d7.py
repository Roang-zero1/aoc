import copy
import re
from collections import namedtuple
from typing import List

from numpy import uint16

from aoc.classes import Result, ResultReturn

Circuit = namedtuple("circuit", "op var1 var2 shift num1 num2")
Circuit.__new__.__defaults__ = (None,) * len(Circuit._fields)


def lshift(circuit, values):
    value = values[circuit.var1] if circuit.var1 else circuit.num1
    return value << circuit.shift


def rshift(circuit, values):
    value = values[circuit.var1] if circuit.var1 else circuit.num1
    return value >> circuit.shift


def bit_and(circuit, values):
    value = values[circuit.var1] if circuit.var1 else circuit.num1
    value2 = values[circuit.var2] if circuit.var2 else circuit.num2
    return value & value2


def bit_or(circuit, values):
    value = values[circuit.var1] if circuit.var1 else circuit.num1
    value2 = values[circuit.var2] if circuit.var2 else circuit.num2
    return value | value2


def bit_not(circuit, values):
    value = values[circuit.var1] if circuit.var1 else circuit.num1
    return ~value


def equals(circuit, values):
    return values[circuit.var1] if circuit.var1 else circuit.num1


def solve_circuits(circuits, values):
    while circuits:
        working_circuits = {
            k: x
            for k, x in circuits.items()
            if x.var1 in values and (x.var2 in values or x.var2 is None)
        }
        for var, circuit in working_circuits.items():
            values[var] = circuit.op(circuit, values)
            del circuits[var]
    return (circuits, values)


def main(puzzle_input: List[str]):
    regex = re.compile(
        r"((?P<value>[0-9]+)|(((?P<o_variable>[a-z]+)|"
        r"(?P<o_number>[0-9]+)) )?((?P<operation>[A-Z]+)"
        r" )?((?P<variable>[a-z]+)|(?P<number>[0-9]+))) -> (?P<output>[a-z]+)"
    )

    operations = {
        "LSHIFT": lshift,
        "RSHIFT": rshift,
        "NOT": bit_not,
        "AND": bit_and,
        "OR": bit_or,
    }

    values = {}
    circuits = {}
    for line in puzzle_input:
        match = regex.match(line)
        if not match:
            print(line)
            exit(0)
        output = match.group("output")
        if match.group("value"):
            values[output] = uint16(match.group("value"))
        else:
            operation = match.group("operation")
            operationf = None
            if operation:
                operationf = operations[operation]
            else:
                operationf = equals
            if operation == "LSHIFT" or operation == "RSHIFT":
                if match.group("o_variable"):
                    circuits[output] = Circuit(
                        operationf,
                        var1=match.group("o_variable"),
                        shift=int(match.group("number")),
                    )
                else:
                    values[output] = operationf(
                        Circuit(
                            None,
                            num1=uint16(match.group("o_number")),
                            shift=int(match.group("number")),
                        )
                    )
            elif operation == "AND" or operation == "OR":
                circuit = Circuit(
                    operationf,
                    var1=match.group("variable") if match.group("variable") else None,
                    var2=match.group("o_variable")
                    if match.group("o_variable")
                    else None,
                    num1=uint16(match.group("number"))
                    if match.group("number")
                    else None,
                    num2=uint16(match.group("o_number"))
                    if match.group("o_number")
                    else None,
                )
                if circuit.num1 and circuit.num2:
                    values[output] = operationf(circuit)
                else:
                    circuits[output] = circuit
            elif operation == "NOT":
                if match.group("variable"):
                    circuits[output] = Circuit(operationf, match.group("variable"))
                else:
                    values[output] = operationf(Circuit(None, match.group("number")))
            else:
                if match.group("variable"):
                    circuits[output] = Circuit(operationf, match.group("variable"))
                else:
                    values[output] = operationf(Circuit(None, match.group("number")))

    original_c = copy.deepcopy(circuits)
    original_v = copy.deepcopy(values)
    circuits, values = solve_circuits(circuits, values)

    result_1 = Result(values["a"], "After first round")

    val_a = values["a"]
    circuits = original_c
    values = original_v
    values["b"] = val_a

    circuits, values = solve_circuits(circuits, values)

    result_2 = Result(values["a"], "After second round")

    return ResultReturn((result_1, result_2))


if __name__ == "__main__":
    raise Exception("Please use the run script")
