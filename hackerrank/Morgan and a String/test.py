import unittest
import my_code


class TestQ(unittest.TestCase):
    def test_case_0(self):
        self.assertEqual(my_code.morganAndString('JACK', 'DANIEL'), 'DAJACKNIEL')
        self.assertEqual(my_code.morganAndString('ABACABA', 'ABACABA'), 'AABABACABACABA')


if __name__ == '__main__':
    unittest.main()
