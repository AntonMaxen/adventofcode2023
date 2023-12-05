def one():
    with open("input.txt") as file:
        data = [line for line in file.readlines()]

    total_sum = 0
    for row in data:
        card_nr, rest = row.split(":")
        winning_numbers, your_numbers = rest.split("|")
        winning_numbers = {int(number.strip()) for number in winning_numbers.split()}
        your_numbers = {int(number.strip()) for number in your_numbers.split()}

        num_matching_numbers = len(your_numbers.intersection(winning_numbers))
        print(num_matching_numbers)
        total_sum += int(2 ** (num_matching_numbers - 1))

    print(total_sum)


def check_win(card_id, all_cards, win_list, dive_deeper):
    card = all_cards[card_id]

    winning_numbers, your_numbers = card.split("|")
    winning_numbers = {int(number.strip()) for number in winning_numbers.split()}
    your_numbers = {int(number.strip()) for number in your_numbers.split()}

    num_matching_numbers = len(your_numbers.intersection(winning_numbers))
    win_list.append(card_id)

    for id in range(card_id + 1, card_id + num_matching_numbers + 1):
        if id < len(all_cards) + 1:
            check_win(id, all_cards, win_list, False)

    if card_id + 1 < len(all_cards) + 1 and dive_deeper:
        check_win(card_id + 1, all_cards, win_list, dive_deeper)


def two():
    with open("input.txt") as file:
        data = [line for line in file.readlines()]
    cards = {}
    for row in data:
        card_nr, rest = row.split(":")
        _, card_id = card_nr.split()
        card_id = int(card_id.strip())
        cards[card_id] = rest

    win_list = []
    check_win(1, cards, win_list, True)
    print(len(win_list))


if __name__ == "__main__":
    two()
