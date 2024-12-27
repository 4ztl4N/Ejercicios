import unittest

from uppercase import to_uppercase

class TestToUpperCase(unittest.TestCase):

  def test_empty_string(self):
    self.assertEqual(to_uppercase(""), "")

  def test_single_word(self):
    self.assertEqual(to_uppercase("hello"), "HELLO")

  def test_multiple_words(self):
    self.assertEqual(to_uppercase("hello world"), "HELLO WORLD")

  def test_with_punctuation(self):
    self.assertEqual(to_uppercase("hello, world!"), "HELLO, WORLD!")

  def test_with_numbers(self):
    self.assertEqual(to_uppercase("hello123"), "HELLO123")

if __name__ == '__main__':
  unittest.main()