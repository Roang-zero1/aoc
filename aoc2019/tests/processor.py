from aoc2019.processor import Processor
import unittest


class Test2019Processor(unittest.TestCase):
    def test_2019_D2_C1(self):
        code = [1, 0, 0, 0, 99]
        processor = Processor(code)
        self.assertListEqual(processor.run(), [2, 0, 0, 0, 99])

    def test_2019_D2_C2(self):
        code = [2, 3, 0, 3, 99]
        processor = Processor(code)
        self.assertListEqual(processor.run(), [2, 3, 0, 6, 99])

    def test_2019_D2_C3(self):
        code = [2, 4, 4, 5, 99, 0]
        processor = Processor(code)
        self.assertListEqual(processor.run(), [2, 4, 4, 5, 99, 9801])

    def test_2019_D2_C4(self):
        code = [1, 1, 1, 4, 99, 5, 6, 0, 99]
        processor = Processor(code)
        self.assertListEqual(processor.run(), [30, 1, 1, 4, 2, 5, 6, 0, 99])

    def test_2019_D2_priming(self):
        code = [1, 0, 0, 0, 99, 2, 3]
        processor = Processor(code)
        self.assertListEqual(processor.run(), [2, 0, 0, 0, 99, 2, 3])
        processor.prime(5, 6)
        self.assertListEqual(processor.run(), [5, 5, 6, 0, 99, 2, 3])
        processor.reset()
        self.assertListEqual(processor.run(), [2, 0, 0, 0, 99, 2, 3])


if __name__ == "__main__":
    unittest.main()
