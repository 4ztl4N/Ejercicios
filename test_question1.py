import unittest

from question1 import q1

class TestQ1(unittest.TestCase):

    def test_easy_range(self):
        valorReal = q1(-5, 15)
        valorEsperado = [7,14]
        self.assertEqual(valorReal, valorEsperado)

    def test_null_range(self):
        valorReal = q1(None, None)
        valorEsperado = []
        self.assertEqual(valorReal, valorEsperado)

    def test_initial_string(self):
        valorReal = q1("5", 15)
        valorEsperado = []
        self.assertEqual(valorReal, valorEsperado)
    
    def test_final_string(self):
        valorReal = q1(5, "15")
        valorEsperado = []
        self.assertEqual(valorReal, valorEsperado)

    def test_valid_range(self):
        valorReal = q1(15, 5)
        valorEsperado = []
        self.assertEqual(valorReal, valorEsperado)

        
if __name__ == '__main__':
    unittest.main()