"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""


def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """

    round_list = [number, number + 1, number + 2]
    return round_list


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """
    for element in rounds_2:  
        rounds_1.append(element)
    return rounds_1


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """

    for current_round in rounds:
        if current_round == number:
            return True
    return False


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """

    total = 0
    for card in hand:
        total = total + card
    return total/len(hand)


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """

    average = card_average(hand)
    first_last_average = (hand[0] + hand[-1])/2
    if average == first_last_average:
        return True
    median = hand[int(len(hand)/2)]
    if average == median:
        return True
    return False


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    even_total = 0
    even_possitions = 0
    odd_possitions = 0
    odd_total = 0
    for index, card in enumerate(hand):
        if (index + 1) % 2 == 0:
            even_total = even_total + card
            even_possitions = even_possitions + 1
        else:
            odd_total = odd_total + card
            odd_possitions = odd_possitions + 1
    even_average = even_total/even_possitions
    odd_average = odd_total/odd_possitions
    if even_average == odd_average:
        return True
    return False


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[-1] == 11:
        hand[-1] = hand[-1] * 2
    return hand
