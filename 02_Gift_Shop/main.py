import fileinput
import re


def main():
    inputs = parse_input()
    print(part_one(inputs))
    print(part_two(inputs))


def part_one(inputs):
    total = 0

    for input in inputs:
        input = input.split("-")
        min = int(input[0])
        max = int(input[1])

        for i in range(min, max + 1):
            numStr = str(i)

            if len(numStr) % 2 != 0:
                continue

            left = numStr[: len(numStr) // 2]
            right = numStr[len(numStr) // 2 :]

            if left == right:
                total += i

    return total


def part_two(inputs):
    total = 0

    for input in inputs:
        input = input.split("-")
        min = int(input[0])
        max = int(input[1])

        for i in range(min, max + 1):
            numStr = str(i)
            if re.fullmatch(r"(.+)\1+", numStr):
                total += i

    return total


def parse_input():
    filename = "input.txt"

    inputs = []

    for line in fileinput.input(files=filename):
        line = line.rstrip()
        line = line.split(",")
        inputs.extend(line)

    return inputs


if __name__ == "__main__":
    main()
