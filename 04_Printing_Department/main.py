import fileinput


def main():
    inputs = parse_input()

    print(part_one(inputs))
    print(part_two(inputs))


def part_one(inputs):
    accessible_count = 0

    for i, line in enumerate(inputs):
        for j, ch in enumerate(line):
            if ch != "@":
                continue

            adjacent_papers = count_adjacent_papers(i, j, inputs, line)

            if adjacent_papers < 4:
                accessible_count += 1

    return accessible_count


def part_two(inputs):
    accessible_count = 0

    while True:
        removable_positions = []
        for i, line in enumerate(inputs):
            for j, ch in enumerate(line):
                if ch != "@":
                    continue
                adjacent_papers = count_adjacent_papers(i, j, inputs, line)

                if adjacent_papers < 4:
                    accessible_count += 1
                    removable_positions.append((i, j))

        if (len(removable_positions)) == 0:
            break

        for pos in removable_positions:
            i = pos[0]
            j = pos[1]

            inputs[i] = inputs[i][:j] + "." + inputs[i][j + 1 :]

        removable_positions = []

    return accessible_count


def count_adjacent_papers(i, j, inputs, line):
    adjacent_papers = 0

    can_left = j > 0
    can_right = j < len(line) - 1

    # Check Left
    if can_left:
        if inputs[i][j - 1] == "@":
            adjacent_papers += 1

    # Check Right
    if can_right:
        if inputs[i][j + 1] == "@":
            adjacent_papers += 1

    # Check Up
    if i != 0:
        if inputs[i - 1][j] == "@":
            adjacent_papers += 1
        if can_left:
            if inputs[i - 1][j - 1] == "@":
                adjacent_papers += 1
        if can_right:
            if inputs[i - 1][j + 1] == "@":
                adjacent_papers += 1
    # Check Down
    if i < len(inputs) - 1:
        if inputs[i + 1][j] == "@":
            adjacent_papers += 1
        if can_left:
            if inputs[i + 1][j - 1] == "@":
                adjacent_papers += 1
        if can_right:
            if inputs[i + 1][j + 1] == "@":
                adjacent_papers += 1
    return adjacent_papers


def parse_input():
    filename = "input.txt"

    inputs = []

    for line in fileinput.input(files=filename):
        inputs.append(line.strip())

    return inputs


if __name__ == "__main__":
    main()
