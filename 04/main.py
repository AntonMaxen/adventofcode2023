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


if __name__ == "__main__":
    one()
