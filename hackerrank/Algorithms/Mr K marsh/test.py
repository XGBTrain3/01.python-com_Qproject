import io
import unittest
from contextlib import redirect_stdout

import solution


class TestQ(unittest.TestCase):
    def test_case_0(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.kMarsh([
                '.x',
                'x.',
            ])
        self.assertEqual(text_trap.getvalue(), 'impossible\n')

    def test_case_1(self):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            solution.kMarsh([
                '.....',
                '.x.x.',
                '.....',
                '.....',
            ])
        self.assertEqual(text_trap.getvalue(), '14\n')


if __name__ == '__main__':
    unittest.main()
