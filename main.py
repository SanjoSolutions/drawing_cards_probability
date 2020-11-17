from itertools import permutations as create_permutations
from multiprocessing import Pool
import os
from functools import reduce
from operator import mul, add
import math


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


def has_drawn_cards(permutation):
    card_counts = determine_card_counts(permutation)
    for card_number, amount in cards_having_drawn:
        if not (card_number in card_counts and card_counts[card_number] == amount):
            return 0
    return 1


def determine_card_counts(permutation):
    card_counts = dict()
    for card_number in permutation:
        if card_number in card_counts:
            card_counts[card_number] += 1
        else:
            card_counts[card_number] = 1
    return card_counts


if __name__ == '__main__':
    number_of_processes = os.cpu_count()
    with Pool(processes=number_of_processes) as pool:
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


        def calculate_number_of_permutations(deck_size, number_of_draws):
            return reduce(mul, range(deck_size - number_of_draws + 1, deck_size + 1)) \
                if number_of_draws >= 1 else 0


        def probability_of_having_drawn_cards_after_n_draws(number_of_draws):
            permutations = create_permutations(deck, number_of_draws)
            permutation_count = calculate_number_of_permutations(len(deck), number_of_draws)
            has_drawn_cards_results = pool.imap_unordered(
                has_drawn_cards,
                permutations,
                chunksize=1024
            )
            count = reduce(add, has_drawn_cards_results, 0)
            return count / float(permutation_count)


        for number_of_draws in range(3, 30 + 1):
            print('After ' + str(number_of_draws) + ' draws: ' + \
                  str(round(probability_of_having_drawn_cards_after_n_draws(number_of_draws) * 100)) + '%'
            )
