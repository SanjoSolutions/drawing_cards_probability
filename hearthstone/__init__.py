from calculate_probability import calculate_probability_for_having_cards_drawn_after_draws


def calculate_probability_for_having_cards_drawn_at_turns(deck, cards_having_drawn_at_turns, starting_first=True):
    cards_having_drawn_after_draws = dict(
        (calculate_cards_drawn_at_turn(turn, starting_first), cards_having_drawn)
        for turn, cards_having_drawn
        in cards_having_drawn_at_turns.items()
    )
    return calculate_probability_for_having_cards_drawn_after_draws(deck, cards_having_drawn_after_draws)


def calculate_cards_drawn_at_turn(turn, starting_first):
    if starting_first:
        return 3 + turn
    else:
        return 4 + turn
