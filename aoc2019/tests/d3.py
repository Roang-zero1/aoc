from aoc2019.d3 import WireTracer
import unittest


class Test2019Day3(unittest.TestCase):
    def test_2019_D3_C1(self):
        wire_1 = ["R8", "U5", "L5", "D3"]
        wire_2 = ["U7", "R6", "D4", "L4"]
        tracer = WireTracer(wire_1, wire_2)
        self.assertEqual(tracer.find_distance(), 6)
        self.assertEqual(tracer.find_timing(), 30)

    def test_2019_D3_C2(self):
        wire_1 = ["R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72"]
        wire_2 = ["U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83"]
        tracer = WireTracer(wire_1, wire_2)
        self.assertEqual(tracer.find_distance(), 159)
        self.assertEqual(tracer.find_timing(), 610)

    def test_2019_D3_C3(self):
        wire_1 = [
            "R98",
            "U47",
            "R26",
            "D63",
            "R33",
            "U87",
            "L62",
            "D20",
            "R33",
            "U53",
            "R51",
        ]
        wire_2 = ["U98", "R91", "D20", "R16", "D67", "R40", "U7", "R15", "U6", "R7"]
        tracer = WireTracer(wire_1, wire_2)
        self.assertEqual(tracer.find_distance(), 135)
        self.assertEqual(tracer.find_timing(), 410)


if __name__ == "__main__":
    unittest.main()
