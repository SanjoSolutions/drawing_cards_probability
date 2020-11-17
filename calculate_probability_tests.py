import unittest

from calculate_probability import calculate_probability


class Test(unittest.TestCase):
    def test_1(self):
        deck = [1, 1, 2, 3, 4]
        c = [1, 2]
        n = 3
        expected_result = 2/5 * (1/4 * 1 + 3/4 * 1/3 * 1 + 2/3 * 0) + \
            1/5 * (2/4 * 1 + 2/4 * (2/3 * 1 + 1/3 * 0)) + \
            2/5 * (2/4 * (1/3 * 1 + 2/3 * 0) + 1/4 * (2/3 * 1 + 1/3 * 0) + 1/4 * 0)
        result = calculate_probability(deck, c, n)
        self.assertEqual(
            expected_result,
            result
        )

    def test_2(self):
        deck = [1, 1, 2, 3, 4]
        c = [1, 2]
        n = len(deck)
        expected_result = 1
        result = calculate_probability(deck, c, n)
        self.assertEqual(
            expected_result,
            result
        )

    def test_3(self):
        deck = [1, 1]
        c = [1, 1]
        n = len(deck)
        expected_result = 1
        result = calculate_probability(deck, c, n)
        self.assertEqual(
            expected_result,
            result
        )


if __name__ == '__main__':
    unittest.main()

