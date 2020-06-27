import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '3',
        '1 0',
        '2 $',
        '3 1',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         "Error Code: integer division or modulo by zero\n"
                         + "Error Code: invalid literal for int() with base 10: '$'\n"
                         + "3\n")


if __name__ == '__main__':
    unittest.main()
