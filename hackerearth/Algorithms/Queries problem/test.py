import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('sys.stdin.readline', side_effect=[
        '8 9',
        '2 2 2 2 2 2 2 2',
        '2',
        '1 3 2',
        '2',
        '1 1 4',
        '2',
        '1 1 8',
        '2',
        '1 8 256',
        '2',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '4\n' +
                         '3\n' +
                         '3\n' +
                         '2\n' +
                         '5\n')


if __name__ == '__main__':
    unittest.main()
