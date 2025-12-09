import fileinput

from shapely.geometry import Point
from shapely.geometry.polygon import Polygon


def main():
    coords = parse_input()
    print(part_one(coords))
    print(part_two(coords))


def part_one(coords):
    areas = set()

    for i, coordA in enumerate(coords):
        for coordB in coords[i + 1 :]:
            areas.add(get_area(coordA, coordB))

    return max(areas)


def part_two(coords):
    areas = set()
    polygon = Polygon(coords)

    for i, coordA in enumerate(coords):
        for coordB in coords[i + 1 :]:
            rect = create_rectangle(coordA[0], coordA[1], coordB[0], coordB[1])

            if polygon.contains(rect):
                areas.add(get_area(coordA, coordB))

    return max(areas)


def create_rectangle(x1, y1, x2, y2):
    return Polygon([(x1, y1), (x1, y2), (x2, y2), (x2, y1)])


def get_area(coordA, coordB):
    # +1 because it's inclusive
    width = abs(coordA[0] - coordB[0]) + 1
    height = abs(coordA[1] - coordB[1]) + 1

    return width * height


def parse_input():
    filename = "input.txt"

    inputs = []

    for line in fileinput.input(files=filename):
        coord = tuple(map(int, line.split(",")))
        inputs.append(coord)

    return inputs


if __name__ == "__main__":
    main()
