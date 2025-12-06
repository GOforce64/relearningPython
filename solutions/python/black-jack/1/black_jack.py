"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    faces = ['J', 'Q','K']
    if card in faces:
        return 10
    if card == 'A':
        return 1
    return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """

    value1 = 0
    value2 = 0
    faces = ['J', 'Q','K']
    
    if card_one in faces:
        value1 = 10
    elif card_one == 'A':
        value1 = 1
    else:
        value1 = int(card_one)

    if card_two in faces:
        value2 = 10
    elif card_two == 'A':
        value2 = 1
    else:
        value2 = int(card_two)

    if value1 == value2:
        return card_one, card_two
    elif value1 > value2:
        return card_one
    else:
        return card_two
    
def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    value1 = 0
    value2 = 0
    faces = ['J', 'Q','K']
    
    if card_one in faces:
        value1 = 10
    elif card_one == 'A':
        value1 = 11
    else:
        value1 = int(card_one)

    if card_two in faces:
        value2 = 10
    elif card_two == 'A':
        value2 = 11
    else:
        value2 = int(card_two)

    if (value1 + value2) > 10:
        return 1
    else:
        return 11


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    tenCards = ['10','J', 'Q','K']
    if (card_one == 'A' and card_two in tenCards) or (card_two == 'A' and card_one in tenCards):
        return True
    return False


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """

    tenCards = ['10','J', 'Q','K']
    if card_one in tenCards and card_two in tenCards:
        return True
    if card_one == card_two:
        return True
    return False


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """

    value1 = 0
    value2 = 0
    doubleDownValues = [9, 10, 11]
    faces = ['J', 'Q', 'K']
    
    if card_one in faces:
        value1 = 10
    elif card_one == 'A':
        value1 = 1
    else:
        value1 = int(card_one)

    if card_two in faces:
        value2 = 10
    elif card_two == 'A':
        value2 = 1
    else:
        value2 = int(card_two)

    if (value1 + value2) in doubleDownValues:
        return True
    return False
