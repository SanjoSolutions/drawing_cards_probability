import unittest

from hearthstone import calculate_probability_for_having_cards_drawn_at_turns


class Test(unittest.TestCase):
    def test_calculate_probability_for_having_cards_drawn_at_turns(self):
        deck = [1, 2, 3]
        cards_having_drawn_at_turns = {
            1: [1, 2, 3],
        }
        starting_first = True
        probability = calculate_probability_for_having_cards_drawn_at_turns(
            deck,
            cards_having_drawn_at_turns,
            starting_first
        )
        self.assertEqual(
            1,
            probability
        )


if __name__ == '__main__':
    unittest.main()
