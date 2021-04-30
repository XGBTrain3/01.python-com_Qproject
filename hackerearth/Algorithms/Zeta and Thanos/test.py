import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch


class TestQ(unittest.TestCase):
    @patch('builtins.input', side_effect=[
        '2 2',
        '7 *',
        '2 5',
        '1 1',
        '2',
        '2 2',
        '2 1',
    ])
    def test_case_0(self, input_mock=None):
        text_trap = io.StringIO()
        with redirect_stdout(text_trap):
            import solution
        self.assertEqual(text_trap.getvalue(),
                         '2 14\n' +
                         '1 9\n')


if __name__ == '__main__':
    unittest.main()
