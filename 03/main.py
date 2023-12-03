from collections import defaultdict


def one():
    with open("input.txt") as file:
        data = [line for line in file.readlines()]

    height = len(data)
    width = len(data[0])

    flat_data = []
    for row in data:
        flat_data.extend(row)
    print(len(flat_data))
    found_links = []
    i = 0
    while i < len(flat_data):
        if not flat_data[i].isnumeric():
            i += 1
            continue
        offset = 0
        while flat_data[i + offset + 1].isnumeric():
            offset += 1
        print(f"found value: {flat_data[i]} index: {i}")
        full_value = "".join(flat_data[i : i + offset + 1])

        y = i // width
        x = i % width
        print(y, x, height, width)
        found_link = False

        for current_offset in range(offset + 1):
            print(f"on: {flat_data[x + current_offset + (y * width)]}")

            for y_check in range(-1, 2):
                for x_check in range(-1, 2):
                    left_bound = x + x_check + current_offset < 0
                    right_bound = x + x_check + current_offset >= width - 1
                    top_bound = y + y_check < 0
                    bottom_bound = y + y_check >= height
                    on_self = (
                        x + current_offset + x_check <= x + offset
                        and x + current_offset + x_check >= x
                    ) and y_check == 0

                    if (left_bound or right_bound) or (top_bound or bottom_bound):
                        continue

                    if on_self:
                        continue

                    found_value = flat_data[
                        (x + current_offset + x_check) + ((y + y_check) * width)
                    ]

                    if found_value != "." and not found_value.isnumeric():
                        print(f"found link: {found_value}")
                        found_link = True

        if found_link:
            print(f"Linked value: {full_value} row: {y} col: {x}")
            found_links.append(int(full_value))

        print("---")
        i += offset + 1

    print(sum(found_links))


def two():
    with open("input.txt") as file:
        data = [line for line in file.readlines()]

    height = len(data)
    width = len(data[0])

    flat_data = []
    for row in data:
        flat_data.extend(row)
    i = 0
    gears = []
    while i < len(flat_data):
        if not flat_data[i] == "*":
            i += 1
            continue

        y = i // width
        x = i % width
        found_values = []
        for y_check in range(-1, 2):
            for x_check in range(-1, 2):
                left_bound = x + x_check < 0
                right_bound = x + x_check >= width - 1
                top_bound = y + y_check < 0
                bottom_bound = y + y_check >= height
                on_self = x_check == 0 and y_check == 0

                if (
                    (left_bound or right_bound)
                    or (top_bound or bottom_bound)
                    or on_self
                ):
                    continue

                found_value = flat_data[(x + x_check) + ((y + y_check) * width)]

                if found_value.isnumeric():
                    found_values.append((x + x_check, y + y_check))

        gears.append(found_values)

        i += 1
    gear_ratios = []
    for i, gear in enumerate(gears):
        coords = defaultdict(list)
        for x, y in gear:
            coords[y].append(x)

        paired_coords = defaultdict(list)
        for y, x_coords in coords.items():
            pair = []
            for i, x in enumerate(x_coords):
                if sum(x_coords[: i + 1]) == sum(list(range(min(x_coords), x + 1))):
                    pair.append(x)
                else:
                    paired_coords[y].append(pair)
                    pair = [x]

            paired_coords[y].append(pair)

        all_pairs = []
        for v in paired_coords.values():
            all_pairs.extend([pair for pair in v])
        print(all_pairs)

        if len(all_pairs) != 2:
            continue

        full_coords = defaultdict(list)
        for row, pairs in paired_coords.items():
            print(pairs)
            for pair in pairs:
                start_point = min(pair)
                end_point = max(pair)
                while True:
                    left_bound = start_point < 0
                    if (
                        left_bound
                        or not flat_data[start_point - 1 + (row * width)].isnumeric()
                    ):
                        break
                    start_point -= 1

                while True:
                    right_bound = end_point >= width - 1
                    if (
                        right_bound
                        or not flat_data[end_point + 1 + (row * width)].isnumeric()
                    ):
                        break
                    end_point += 1

                full_coords[row].append([start_point, end_point])

        gear_pairs = []
        for y, v in full_coords.items():
            for pair in v:
                gear_pairs.append(
                    int(
                        "".join(
                            [
                                flat_data[c + (y * width)]
                                for c in list(range(pair[0], pair[-1] + 1))
                            ]
                        )
                    )
                )
        gear_ratios.append(gear_pairs[0] * gear_pairs[1])

    print(sum(gear_ratios))


if __name__ == "__main__":
    two()
