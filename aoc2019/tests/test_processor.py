import unittest

from aoc2019.processor import Processor, ResultMode
from aoc.unittest import LoggedTestCase


class Test2019Processor(unittest.TestCase):
    def test_simple_addition(self):
        code = [1, 0, 0, 0, 99]
        processor = Processor(code)
        self.assertTupleEqual(processor.run(), (ResultMode.FINISHED, [2, 0, 0, 0, 99]))

    def test_simple_multiplication(self):
        code = [2, 3, 0, 3, 99]
        processor = Processor(code)
        self.assertTupleEqual(processor.run(), (ResultMode.FINISHED, [2, 3, 0, 6, 99]))

    def test_simple_multiplication_2(self):
        code = [2, 4, 4, 5, 99, 0]
        processor = Processor(code)
        self.assertTupleEqual(
            processor.run(), (ResultMode.FINISHED, [2, 4, 4, 5, 99, 9801])
        )

    def test_chained_operation(self):
        code = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        processor = Processor(code)
        self.assertTupleEqual(
            processor.run(), (ResultMode.FINISHED, [30, 1, 1, 4, 2, 5, 6, 0, 99])
        )

    def test_priming(self):
        code = [1, 0, 0, 0, 99, 2, 3]
        processor = Processor(code)
        self.assertTupleEqual(
            processor.run(), (ResultMode.FINISHED, [2, 0, 0, 0, 99, 2, 3])
        )
        processor.prime(5, 6)
        self.assertTupleEqual(
            processor.run(), (ResultMode.FINISHED, [5, 5, 6, 0, 99, 2, 3])
        )
        processor.reset()
        self.assertTupleEqual(
            processor.run(), (ResultMode.FINISHED, [2, 0, 0, 0, 99, 2, 3])
        )


class Test2019ProcessorV2(unittest.TestCase):
    def test_parameter_modes(self):
        code = [1002, 4, 3, 4, 33]
        processor = Processor(code)
        self.assertTupleEqual(
            processor.run(), (ResultMode.FINISHED, [1002, 4, 3, 4, 99])
        )

    def test_input_output(self):
        code = [3, 0, 4, 0, 99]
        value = 50
        processor = Processor(code)
        self.assertTupleEqual(processor.run(), (ResultMode.INPUT, None))
        self.assertTupleEqual(
            processor.continue_operation(value), (ResultMode.OUTPUT, value)
        )
        self.assertTupleEqual(
            processor.continue_operation(), (ResultMode.FINISHED, [50, 0, 4, 0, 99])
        )

    def test_negative_integers(self):
        code = [1101, 100, -1, 4, 0]
        processor = Processor(code)
        self.assertTupleEqual(
            processor.run(), (ResultMode.FINISHED, [1101, 100, -1, 4, 99])
        )


class Test2019ProcessorV3(LoggedTestCase):
    def test_equals_position(self):
        code = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
        processor = Processor(code)
        self.assertTupleEqual(processor.run(), (ResultMode.INPUT, None))
        self.assertTupleEqual(processor.continue_operation(8), (ResultMode.OUTPUT, 1))
        self.assertTupleEqual(
            processor.continue_operation(),
            (ResultMode.FINISHED, [3, 9, 8, 9, 10, 9, 4, 9, 99, 1, 8]),
        )
        processor.reset()
        self.assertTupleEqual(processor.run(), (ResultMode.INPUT, None))
        self.assertTupleEqual(processor.continue_operation(9), (ResultMode.OUTPUT, 0))
        self.assertTupleEqual(
            processor.continue_operation(),
            (ResultMode.FINISHED, [3, 9, 8, 9, 10, 9, 4, 9, 99, 0, 8]),
        )

    def test_less_than_position(self):
        code = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
        processor = Processor(code)
        self.assertTupleEqual(processor.run(), (ResultMode.INPUT, None))
        self.assertTupleEqual(processor.continue_operation(7), (ResultMode.OUTPUT, 1))
        self.assertTupleEqual(
            processor.continue_operation(),
            (ResultMode.FINISHED, [3, 9, 7, 9, 10, 9, 4, 9, 99, 1, 8]),
        )
        processor.reset()
        self.assertTupleEqual(processor.run(), (ResultMode.INPUT, None))
        self.assertTupleEqual(processor.continue_operation(8), (ResultMode.OUTPUT, 0))
        self.assertTupleEqual(
            processor.continue_operation(),
            (ResultMode.FINISHED, [3, 9, 7, 9, 10, 9, 4, 9, 99, 0, 8]),
        )
        processor.reset()
        self.assertTupleEqual(processor.run(), (ResultMode.INPUT, None))
        self.assertTupleEqual(processor.continue_operation(9), (ResultMode.OUTPUT, 0))
        self.assertTupleEqual(
            processor.continue_operation(),
            (ResultMode.FINISHED, [3, 9, 7, 9, 10, 9, 4, 9, 99, 0, 8]),
        )

    def test_equals_immediate(self):
        code = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
        processor = Processor(code)
        self.assertTupleEqual(processor.run(), (ResultMode.INPUT, None))
        self.assertTupleEqual(processor.continue_operation(8), (ResultMode.OUTPUT, 1))
        self.assertTupleEqual(
            processor.continue_operation(),
            (ResultMode.FINISHED, [3, 3, 1108, 1, 8, 3, 4, 3, 99]),
        )
        processor.reset()
        self.assertTupleEqual(processor.run(), (ResultMode.INPUT, None))
        self.assertTupleEqual(processor.continue_operation(9), (ResultMode.OUTPUT, 0))
        self.assertTupleEqual(
            processor.continue_operation(),
            (ResultMode.FINISHED, [3, 3, 1108, 0, 8, 3, 4, 3, 99]),
        )

    def test_less_than_immediate(self):
        code = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
        processor = Processor(code)
        self.assertTupleEqual(processor.run(), (ResultMode.INPUT, None))
        self.assertTupleEqual(processor.continue_operation(7), (ResultMode.OUTPUT, 1))
        self.assertTupleEqual(
            processor.continue_operation(),
            (ResultMode.FINISHED, [3, 3, 1107, 1, 8, 3, 4, 3, 99]),
        )
        processor.reset()
        self.assertTupleEqual(processor.run(), (ResultMode.INPUT, None))
        self.assertTupleEqual(processor.continue_operation(8), (ResultMode.OUTPUT, 0))
        self.assertTupleEqual(
            processor.continue_operation(),
            (ResultMode.FINISHED, [3, 3, 1107, 0, 8, 3, 4, 3, 99]),
        )
        processor.reset()
        self.assertTupleEqual(processor.run(), (ResultMode.INPUT, None))
        self.assertTupleEqual(processor.continue_operation(9), (ResultMode.OUTPUT, 0))
        self.assertTupleEqual(
            processor.continue_operation(),
            (ResultMode.FINISHED, [3, 3, 1107, 0, 8, 3, 4, 3, 99]),
        )

    def test_jumps_immediate(self):
        code = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
        processor = Processor(code)
        self.assertTupleEqual(processor.run(), (ResultMode.INPUT, None))
        self.assertTupleEqual(processor.continue_operation(0), (ResultMode.OUTPUT, 0))
        self.assertTupleEqual(
            processor.continue_operation(),
            (
                ResultMode.FINISHED,
                [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, 0, 0, 1, 9],
            ),
        )
        processor.reset()
        self.assertTupleEqual(processor.run(), (ResultMode.INPUT, None))
        self.assertTupleEqual(processor.continue_operation(1), (ResultMode.OUTPUT, 1))
        self.assertTupleEqual(
            processor.continue_operation(),
            (
                ResultMode.FINISHED,
                [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, 1, 1, 1, 9],
            ),
        )

    def test_jumps_position(self):
        code = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
        processor = Processor(code)
        self.assertTupleEqual(processor.run(), (ResultMode.INPUT, None))
        self.assertTupleEqual(processor.continue_operation(0), (ResultMode.OUTPUT, 0))
        self.assertTupleEqual(
            processor.continue_operation(),
            (ResultMode.FINISHED, [3, 3, 1105, 0, 9, 1101, 0, 0, 12, 4, 12, 99, 0]),
        )
        processor.reset()
        self.assertTupleEqual(processor.run(), (ResultMode.INPUT, None))
        self.assertTupleEqual(processor.continue_operation(1), (ResultMode.OUTPUT, 1))
        self.assertTupleEqual(
            processor.continue_operation(),
            (ResultMode.FINISHED, [3, 3, 1105, 1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]),
        )

    def test_complex(self):
        code = [
            3,
            21,
            1008,
            21,
            8,
            20,
            1005,
            20,
            22,
            107,
            8,
            21,
            20,
            1006,
            20,
            31,
            1106,
            0,
            36,
            98,
            0,
            0,
            1002,
            21,
            125,
            20,
            4,
            20,
            1105,
            1,
            46,
            104,
            999,
            1105,
            1,
            46,
            1101,
            1000,
            1,
            20,
            4,
            20,
            1105,
            1,
            46,
            98,
            99,
        ]
        processor = Processor(code)
        self.assertTupleEqual(processor.run(), (ResultMode.INPUT, None))
        self.assertTupleEqual(processor.continue_operation(7), (ResultMode.OUTPUT, 999))
        code_case_1 = code.copy()
        code_case_1[21] = 7
        self.assertTupleEqual(
            processor.continue_operation(), (ResultMode.FINISHED, code_case_1)
        )
        processor.reset()
        self.assertTupleEqual(processor.run(), (ResultMode.INPUT, None))
        self.assertTupleEqual(
            processor.continue_operation(8), (ResultMode.OUTPUT, 1000)
        )
        code_case_2 = code.copy()
        code_case_2[20] = 1000
        code_case_2[21] = 8
        self.assertTupleEqual(
            processor.continue_operation(), (ResultMode.FINISHED, code_case_2)
        )
        processor.reset()
        self.assertTupleEqual(processor.run(), (ResultMode.INPUT, None))
        self.assertTupleEqual(
            processor.continue_operation(9), (ResultMode.OUTPUT, 1001)
        )
        code_case_3 = code.copy()
        code_case_3[20] = 1001
        code_case_3[21] = 9
        self.assertTupleEqual(
            processor.continue_operation(), (ResultMode.FINISHED, code_case_3)
        )


if __name__ == "__main__":
    unittest.main()
