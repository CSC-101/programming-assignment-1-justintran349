import data
import hw1
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_vowel_count_1(self):
        input = 'hello'
        result = hw1.vowel_count(input)
        expected = 2
        self.assertEqual(expected, result)
    def test_vowel_count_2(self):
        input = 'window'
        result = hw1.vowel_count(input)
        expected = 2
        self.assertEqual(expected, result)

    # Part 2
    def test_short_list_1(self):
        input[[1,2],[3,4,5],[6,7]]
        result = hw1.short_lists(input)
        expected=[[1,2],[6,7]]
        self.assertEqual(expected, result)

    def test_short_list_1(self):
        input[[2, 3], [4, 5, 6], [7, 8]]
        result = hw1.short_lists(input)
        expected = [[2, 3], [7, 8]]
        self.assertEqual(expected, result)

            # Part 3


    # Part 4


    # Part 5


    # Part 6


    # Part 7


    # Part 8





if __name__ == '__main__':
    unittest.main()
