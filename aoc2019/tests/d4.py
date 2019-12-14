from aoc2019.d4 import test_password
import unittest


class Test2019Day4(unittest.TestCase):
    def test_2019_D4_C1(self):
        self.assertTrue(test_password(111111))

    def test_2019_D4_C2(self):
        self.assertFalse(test_password(223450))

    def test_2019_D4_C3(self):
        self.assertFalse(test_password(123789))

    def test_2019_D4_C4(self):
        self.assertTrue(test_password(112233))

    def test_2019_D4_C5(self):
        self.assertFalse(test_password(123444, True))

    def test_2019_D4_C6(self):
        self.assertTrue(test_password(111122, True))

    def test_2019_D4_C7(self):
        self.assertFalse(test_password(222333, True))


if __name__ == "__main__":
    unittest.main()
