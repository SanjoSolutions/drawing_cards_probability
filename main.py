from calculate_probability import calculate_probability

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
    A,
    B,
    B,
    C,
    D
]

for number_of_draws in range(3 + 10, 30 + 1):
    probability = calculate_probability(deck, cards_having_drawn, number_of_draws)
    print('After ' + str(number_of_draws) + ' draws: ' + str(round(probability * 100)) + '%')
