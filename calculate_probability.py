def calculate_probability(deck, cards_to_draw, total_number_of_cards_to_draw):
    number_of_cards_drawn = 0

    verify_that_all_cards_are_in_deck(deck, cards_to_draw)
    deck = anonymize_non_drawn_cards(deck, cards_to_draw)

    result = p(deck, cards_to_draw, number_of_cards_drawn, total_number_of_cards_to_draw)
    return result


def verify_that_all_cards_are_in_deck(deck, cards):
    if not all_cards_are_in_deck(deck, cards):
        raise AssertionError('Some cards are not in deck. Therefore all cards cannot be drawn from deck.')


def all_cards_are_in_deck(deck, cards):
    deck_card_counts = determine_card_counts(deck)
    card_counts = determine_card_counts(cards)
    return all(
        card in deck_card_counts and deck_card_counts[card] >= amount
        for card, amount
        in card_counts.items()
    )


def determine_card_counts(cards):
    card_counts = dict()
    for card in cards:
        if card in card_counts:
            card_counts[card] += 1
        else:
            card_counts[card] = 1
    return card_counts


def anonymize_non_drawn_cards(deck, cards):
    cards = set(cards)
    return [
        card if card in cards else None
        for card
        in deck
    ]


def p(deck, cards_to_draw, number_of_cards_drawn, total_number_of_cards_to_draw):
    len_c = len(cards_to_draw)
    if len_c == 0:
        return 1
    elif number_of_cards_drawn == total_number_of_cards_to_draw or \
         less_cards_left_to_draw_than_needed(len_c, number_of_cards_drawn, total_number_of_cards_to_draw):
        return 0

    number_of_cards_drawn += 1

    probability = 0
    number_of_cards_in_deck = float(len(deck))
    deck_card_counts = determine_card_counts(deck)
    cards_to_draw_counts = determine_card_counts(cards_to_draw)
    for card in set(cards_to_draw):
        cards_to_draw_for_recursive_call = cards_to_draw.copy()
        cards_to_draw_for_recursive_call.remove(card)
        deck_for_recursive_call = deck.copy()
        deck_for_recursive_call.remove(card)
        deck_for_recursive_call = anonymize_non_drawn_cards(deck_for_recursive_call, cards_to_draw_for_recursive_call)
        a = deck_card_counts[card] / number_of_cards_in_deck
        b = a * p(
            deck_for_recursive_call,
            cards_to_draw_for_recursive_call,
            number_of_cards_drawn,
            total_number_of_cards_to_draw
        )
        probability += b

    other_cards = [
        card
        for card
        in deck
        if card not in cards_to_draw
    ]
    number_of_other_cards = len(other_cards)
    if number_of_other_cards >= 1:
        deck_for_recursive_call = deck.copy()
        deck_for_recursive_call.remove(None)
        a = (number_of_other_cards / number_of_cards_in_deck)
        b = a * p(deck_for_recursive_call, cards_to_draw, number_of_cards_drawn, total_number_of_cards_to_draw)
        probability += b

    return probability


def less_cards_left_to_draw_than_needed(number_of_cards_needed, number_of_cards_drawn, total_number_of_cards_to_draw):
    cards_left_to_draw = total_number_of_cards_to_draw - number_of_cards_drawn
    return number_of_cards_needed > cards_left_to_draw
