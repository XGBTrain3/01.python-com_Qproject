import unittest

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(solution.hurdleRace(4, [1, 6, 3, 5, 2]), 2)

    def test_case_1(self):
        self.assertEqual(solution.hurdleRace(7, [2, 5, 4, 5, 2]), 0)


if __name__ == '__main__':
    unittest.main()
