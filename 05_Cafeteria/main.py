import fileinput
from itertools import chain


def main():
    inputs = parse_input()

    ranges = [get_range(x) for x in inputs if "-" in x]
    ingredient_ids = [int(x) for x in inputs if "-" not in x and x != ""]

    print(part_one(ranges, ingredient_ids))
    print(part_two(ranges))


def part_one(ranges, ingredient_ids):
    fresh_count = 0

    for id in ingredient_ids:
        for pair in ranges:
            if pair[0] <= id <= pair[1]:
                fresh_count += 1
                break

    return fresh_count


def part_two(ranges):
    ranges.sort(key=lambda x: x[0])

    merged_ranges = []

    for start, end in ranges:
        if not merged_ranges or merged_ranges[-1][1] < start:
            merged_ranges.append([start, end])
        else:
            merged_ranges[-1][1] = max(merged_ranges[-1][1], end)

    fresh_ids = sum(end - start + 1 for start, end in merged_ranges)

    return fresh_ids


def get_range(rangeStr):
    return list(map(int, rangeStr.split("-")))


def parse_input():
    filename = "input.txt"

    inputs = []

    for line in fileinput.input(files=filename):
        inputs.append(line.strip())

    return inputs


if __name__ == "__main__":
    main()
