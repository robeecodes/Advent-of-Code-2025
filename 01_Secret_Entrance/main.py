import fileinput


def main():
    inputs = parse_input()

    print(f"Part 1: {part_one(inputs)}")

    print(f"Part 2: {part_two(inputs)}")


def part_one(inputs):
    position = 50
    counter = 0

    for input in inputs:
        direction = input[0]  # Get the direction as 'L' or 'R'
        turns = int(input[1:])  # Get the number of turns and convert to int

        for _ in range(turns):
            # Update position based on direction
            if direction == "L":
                position -= 1
                if position < 0:  # Wrap around to 99
                    position = 99
            elif direction == "R":
                position += 1
                if position > 99:  # Wrap around to 0
                    position = 0

        # Check if the final position is 0 after all turns
        if position == 0:
            counter += 1

    return counter


def part_two(inputs):
    position = 50
    counter = 0

    for input in inputs:
        direction = input[0]
        turns = int(input[1:])

        for _ in range(turns):
            if direction == "L":
                position -= 1
                if position < 0:
                    position = 99

            if direction == "R":
                position += 1
                if position > 99:
                    position = 0

            if position == 0:
                counter += 1

    return counter


def parse_input():
    filename = "input.txt"

    inputs = []

    for line in fileinput.input(files=filename):
        inputs.append(line)

    return inputs


if __name__ == "__main__":
    main()
