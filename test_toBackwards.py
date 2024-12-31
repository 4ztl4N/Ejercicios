import unittest

from toBackwards import palindromo
from toBackwards import palindrom

class TestToUpperCase(unittest.TestCase):

    def test_empty_word(self):
        self.assertEqual(palindromo(""), True)

    def test_wrong_palindromo(self):
        self.assertEqual(palindromo("hola"), False)

    def test_null_word(self):
        self.assertEqual(palindromo(None),False)

    def test_word_with_number(self):
        self.assertEqual(palindromo("4ztl4n"), False)

    def test_empty_array(self):
        self.assertEqual(palindromo([]),False)

    def test_filled_array(self):
        self.assertEqual(palindromo([384,29847,74728]),False)

    def test_good_palindromo(self):
        self.assertEqual(palindrom("oso"), True)
        
if __name__ == '__main__':
    unittest.main()