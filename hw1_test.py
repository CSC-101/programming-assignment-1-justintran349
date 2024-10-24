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
        input'[[1,2],[3,4,5],[6,7]]'
        result = hw1.short_lists(input)
        expected=[[1,2],[6,7]]
        self.assertEqual(expected, result)

    def test_short_list_2(self):
        input[[2, 3], [4, 5, 6], [7, 8]]
        result = hw1.short_lists(input)
        expected = [[2, 3], [7, 8]]
        self.assertEqual(expected, result)

    # Part 3
    def test_ascending_pairs_1(self):
        input[[4, 1], [4, 5]]
        result = hw1.ascending_pairs(input)
        expected = [[1,3], [4,5]]
        self.assertEqual(expected, result)

    def test_ascending_pairs_1(self):
        input[[4, 1], [4, 5]]
        result = hw1.ascending_pairs(input)
        expected = [[1,3], [4,5]]
        self.assertEqual(expected, result)
    # Part 4
    def test_add_prices_1(self):
        input(3,300)
        result = hw1.add_prices(input)
        expected = 6
        self.assertEqual(expected, result)

    def test_add_prices_2(self):
        input(4,350)
        result = hw1.add_prices(input)
        expected = 7.50
        self.assertEqual(expected, result)
    # Part 5
    def test_rectangle_area_1(self):
        input(1,5)(6,1)
        result = hw1.rectangle_area(input)
        expected = 20
        self.assertEqual(expected, result)

    def test_rectangle_area_2(self):
        input(2,5)(4,1)
        result = hw1.rectangle_area(input)
        expected = 9
        self.assertEqual((expected, result))
    # Part 6
    def test_books_by_author_1(self):
        input("ABCs", ["John Doe"])
        result = hw1.books_by_author(input)
        expected = "ABCs by John Doe"
        self.assertEqual(expected, result)

    def test_books_by_author_2(self):
        input("123s", ["John Doe"])
        result = hw1.books_by_author(input)
        expected = "123s by John Doe"
        self.assertEqual(expected, result)
    # Part 7
    def test_circle_bound_1(self):
        input(3.5,3.0)
        result = hw1.circle_bound(input)
        expected = 3.20
    # Part 8
    def below_average_pay_1(self):
        input("George", 45)("bob", 35)
        result = hw1.below_pay_average(input)
        expected = 40
        self.assertEqual(expected,result)

    def below_average_pay_2(self):
        input("George", 55)("bob", 45)
        result = hw1.below_pay_average(input)
        expected = 50
        self.assertEqual(expected,result)

if __name__ == '__main__':
    unittest.main()
