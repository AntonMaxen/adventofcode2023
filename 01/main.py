def one():
    with open("input.txt") as file:
        lines = [line.strip() for line in file.readlines()]
    pairs = []
    for line in lines:
        numbers = [n for n in line if n.isnumeric()]
        pairs.append(int(f"{numbers[0]}{numbers[-1]}"))

    print(sum(pairs))
    ...


def two():
    number_map = dict(
        one=1, two=2, three=3, four=4, five=5, six=6, seven=7, eight=8, nine=9
    )

    with open("input.txt") as file:
        lines = [line.strip() for line in file.readlines()]

    pairs = []
    for line in lines:
        for number_string, value in number_map.items():
            line = line.replace(number_string, f"{number_string}{value}{number_string}")

        numbers = [n for n in line if n.isnumeric()]
        pairs.append(int(f"{numbers[0]}{numbers[-1]}"))

    print(sum(pairs))


if __name__ == "__main__":
    two()
