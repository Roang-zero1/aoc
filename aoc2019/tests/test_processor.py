from aoc2019.processor import Processor, ResultMode
import unittest


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


if __name__ == "__main__":
    unittest.main()
