from collections import defaultdict
from functools import reduce

CARD_ORDER = "23456789TJQKA"


def is_five_of_kind(cards):
    return len(set(cards)) == 1


def is_four_of_kind(cards):
    return bool([c for c in set(cards) if cards.count(c) == 4])


def is_full_house(cards):
    if len(set(cards)) != 2:
        return False

    return len([c for c in set(cards) if cards.count(c) in [2, 3]]) == 2


def is_three_of_kind(cards):
    return bool([c for c in set(cards) if cards.count(c) == 3])


def is_two_pair(cards):
    return len(set(cards)) == 3


def is_one_pair(cards):
    return len(set(cards)) == 4


def check_hand(cards):
    if is_five_of_kind(cards):
        return 6
    elif is_four_of_kind(cards):
        return 5
    elif is_full_house(cards):
        return 4
    elif is_three_of_kind(cards):
        return 3
    elif is_two_pair(cards):
        return 2
    elif is_one_pair(cards):
        return 1
    else:
        return 0


def hand_value(cards):
    hand_value = 0
    for i, c in enumerate(cards):
        card_order = CARD_ORDER.find(c) + 1
        hand_value += int(card_order * (10 ** ((len(cards) - i) * 3)))

    return hand_value


def one():
    with open("input.txt") as file:
        data = [line.strip() for line in file.readlines() if line.strip()]

    player_hands = []
    for player in data:
        hand = player.split()
        cards, bid = hand
        cards = cards.strip()
        player_hands.append((cards, int(bid)))

    s_hands = sorted(player_hands, key=lambda c: (check_hand(c[0]), hand_value(c[0])))

    with open("res.txt", "w") as t:
        t.write(
            "\n".join(
                [f"{c[0]} - {check_hand(c[0])} - {hand_value(c[0])}" for c in s_hands]
            )
        )

    # hh = defaultdict(list)

    # for cards, bid in player_hands:
    #     hh[check_hand(cards)].append(cards)

    # print(sorted(hh[0], key=lambda c: hand_value(c)))

    # print(s_hands[:10])

    scaled_bids = [hand[1] * rank for rank, hand in enumerate(s_hands, 1)]
    print(sum(scaled_bids))
    # bid = int(bid.strip())
    # print(cards, check_hand(cards))


def two():
    with open("input.txt") as file:
        data = [line.strip() for line in file.readlines() if line.strip()]


if __name__ == "__main__":
    one()
