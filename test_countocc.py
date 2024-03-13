import unittest
from countocc import count_occurrences

class TestCountOccurrences(unittest.TestCase):
    def test_single_word(self):
        result = count_occurrences("testthisstring")
        self.assertEqual(result, {'t': 4, 'e': 1, 's': 3, 'h': 1, 'i': 2, 'r': 1, 'n': 1, 'g': 1})

    def test_multiple_words(self):
        result = count_occurrences("what about this one?")
        self.assertEqual(result, {'w': 1, 'h': 2, 'a': 2, 't': 3, 'b': 1, 'o': 2, 'u': 1, 'i': 1, 's': 1, 'n': 1, 'e': 1})

    def test_empty_string(self):
        result = count_occurrences("")
        self.assertEqual(result, {})

    def test_no_alphabetic_characters(self):
        result = count_occurrences("12345!@#$%")
        self.assertEqual(result, {})

if __name__ == '__main__':
    unittest.main()