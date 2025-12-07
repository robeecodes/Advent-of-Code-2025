import fileinput
from operator import indexOf
from re import L


def main():
    inputs = parse_input()

    pos = (0, indexOf(inputs[0], "S"))

    print(part_one(pos, inputs))
    print(part_two(pos, inputs))


def part_one(pos, inputs):
    splits = 0

    beams = {pos[1]}

    for row in inputs[1:]:
        next_row = set()
        for beam in beams:
            if row[beam] == ".":
                next_row.add(beam)
            else:
                splits += 1
                next_row.add(beam - 1)
                next_row.add(beam + 1)

        beams = next_row

    return splits


def part_two(pos, inputs):
    beams = dict()

    beams[pos[1]] = 1

    for row in inputs[1:]:
        for beam in beams.copy():
            if row[beam] == "^":
                if beam - 1 in beams:
                    beams[beam - 1] += beams[beam]
                else:
                    beams[beam - 1] = beams[beam]
                if beam + 1 in beams:
                    beams[beam + 1] += beams[beam]
                else:
                    beams[beam + 1] = beams[beam]
                beams.pop(beam)

    splits = 0

    for beam in beams:
        splits += beams[beam]

    return splits


def parse_input():
    filename = "input.txt"

    inputs = []

    for input in fileinput.input(files=filename):
        inputs.append(input)

    return inputs


if __name__ == "__main__":
    main()
