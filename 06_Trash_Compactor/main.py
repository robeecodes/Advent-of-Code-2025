import fileinput
from functools import reduce
from operator import add, mul


def main():
    inputs = list(zip(*[row.split() for row in parse_input()]))
    inputs_two = parse_input()
    operators = inputs_two[-1]

    print(part_one(inputs))
    print(part_two(inputs_two, operators))


def part_one(inputs):
    total = 0
    for input in inputs:
        operator = input[-1]

        nums = map(int, input[:-1])

        if operator == "*":
            total += reduce(mul, nums)
        elif operator == "+":
            total += reduce(add, nums)
    return total


def part_two(inputs, operators):
    total = 0

    cols = []

    for input in inputs:
        cols.append(list(input))

    colLength = len(max(cols, key=len))

    for line in cols:
        while len(line) < colLength:
            line.append("")

    cols = list(zip(*cols))

    operator = ""
    acc = 0

    for col in cols:
        if "".join(col).strip() == "":
            operator = ""
            total += acc
            acc = 0
            continue

        if col[-1] == "*" or col[-1] == "+":
            operator = col[-1]
            acc = int("".join(col[:-1]))

        else:
            num = int("".join(col[:-1]))

            if operator == "*":
                if acc == 0:
                    acc = 1
                acc *= num

            if operator == "+":
                acc += num

    return total


def parse_input():
    filename = "input.txt"

    inputs = []

    for line in fileinput.input(files=filename):
        inputs.append(line)

    return inputs


if __name__ == "__main__":
    main()
