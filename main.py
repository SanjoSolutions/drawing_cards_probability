from itertools import permutations as create_permutations

deck = [
    1,
    2,
    2,
    3,
    3,
    4,
    4,
    5,
    5,
    6,
    6,
    7,
    7,
    8,
    8,
    9,
    9,
    10,
    10,
    11,
    12,
    13,
    13,
    14,
    14,
    15,
    15,
    16,
    17,
    18
]

A = 9  # Aldrachi Warblades
B = 3  # Twin Slice
C = 5  # Chaos Strike
D = 18  # Il'gynoth

cards_having_drawn = [
    # card number, amount
    (A, 1),
    (B, 2),
    (C, 1),
    (D, 1)
]


def has_drawn_cards(cards_having_drawn, permutation):
    for card_number, amount in cards_having_drawn:
        if permutation.count(card_number) != amount:
            return False
    return True


def probability_of_having_drawn_cards_after_n_draws(cards_having_drawn, number_of_draws):
    permutations = create_permutations(deck, number_of_draws)
    count = 0
    permutation_count = 0
    for permutation in permutations:
        if has_drawn_cards(cards_having_drawn, permutation):
            count += 1
        permutation_count += 1
    return count / float(permutation_count)


for number_of_draws in range(30 + 1):
    print('After ' + str(number_of_draws) + ' draws: ' + \
          str(round(probability_of_having_drawn_cards_after_n_draws(cards_having_drawn, number_of_draws) * 100)) + '%'
    )
