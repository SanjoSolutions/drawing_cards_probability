from hearthstone.deck import deck
from hearthstone import calculate_probability_for_having_cards_drawn_at_turns

A = 2  # Spirit Jailer
B = 8  # Wandmaker
C = 6  # Manafeeder Panthara

cards_having_drawn_at_turns = {
    1: [A],
    2: [B],
    3: [C]
}

starting_first = True
probability = calculate_probability_for_having_cards_drawn_at_turns(
    deck,
    cards_having_drawn_at_turns,
    starting_first
)
print('Probability: ' + str(round(probability * 100)) + '%')
