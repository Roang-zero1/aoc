from aoc2019.d1 import calculate_fuel, calculate_total_fuel
import unittest


class Test2019Day1(unittest.TestCase):
    def test_2019_D1_C1(self):
        self.assertTupleEqual(calculate_fuel(12), (2, 2))

    def test_2019_D1_C2(self):
        self.assertTupleEqual(calculate_fuel(14), (2, 2))

    def test_2019_D1_C3(self):
        self.assertTupleEqual(calculate_fuel(1969), (654, 966))

    def test_2019_D1_C4(self):
        self.assertTupleEqual(calculate_fuel(100756), (33583, 50346))

    def test_2019_D1_sum(self):
        masses = [12, 14, 1969, 100756]
        self.assertTupleEqual(calculate_total_fuel(masses), (34241, 51316))


if __name__ == "__main__":
    unittest.main()
