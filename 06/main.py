from functools import reduce


def one():
    with open("input.txt") as file:
        data = (line.strip() for line in file.readlines() if line.strip())
    time, distances = data
    times = [int(t.strip()) for t in time.split(":")[1].split()]
    distances = [int(t.strip()) for t in distances.split(":")[1].split()]

    wins = []
    for i, time in enumerate(times):
        distance = distances[i]
        win = 0
        for i in range(time + 1):
            if (time - i) * i > distance:
                win += 1

        wins.append(win)

    p1 = reduce(lambda x, y: x * y, wins)
    print(p1)


def two():
    with open("input.txt") as file:
        data = (line.strip() for line in file.readlines() if line.strip())
    time, distances = data
    time = int("".join([t.strip() for t in time.split(":")[1].split()]))
    distance = int("".join([t.strip() for t in distances.split(":")[1].split()]))

    win = 0
    for i in range(time + 1):
        if (time - i) * i > distance:
            win += 1

    print(win)


if __name__ == "__main__":
    two()
