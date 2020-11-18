from calculate_probability import calculate_probability
from hearthstone.deck import deck

A = 9  # Aldrachi Warblades
B = 3  # Twin Slice
C = 5  # Chaos Strike
D = 12  # Il'gynoth

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
