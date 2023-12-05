import json
from collections import defaultdict


def one():
    with open("input.txt") as file:
        data = [line.strip() for line in file.readlines() if line.strip()]

    seeds = [int(n.strip()) for n in data[0].split(":")[1].split()]
    maps = defaultdict(list)
    map_name = None
    for row in data:
        if "map" in row:
            map_name, _ = row.split()
            continue

        if map_name:
            nr = [int(n.strip()) for n in row.split()]
            maps[map_name].append(
                {"min": nr[1], "max": nr[1] + abs(nr[2] - 1), "offset": nr[1] - nr[0]}
            )

    map_values = []
    for seed in seeds:
        map_value = seed
        for name, s_maps in maps.items():
            for map in s_maps:
                if map["min"] <= map_value <= map["max"]:
                    map_value = map_value - map["offset"]
                    break

        map_values.append(map_value)

    print(min(map_values))


if __name__ == "__main__":
    one()
