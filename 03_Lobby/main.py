import fileinput
from queue import Empty


def main():
    inputs = parse_input()
    print(part_one(inputs))
    print(part_two(inputs))


def part_one(inputs):
    total = 0

    for input in inputs:
        nums = [int(num) for num in list(input)]

        maxNumPos = nums.index(max(nums))
        secondMaxNumPos = 0

        if maxNumPos == len(nums) - 1:
            secondMaxNumPos = maxNumPos
            maxNumPos = nums[:secondMaxNumPos].index(max(nums[:secondMaxNumPos]))
        else:
            secondMaxNumPos = nums.index(max(nums[maxNumPos + 1 :]))

        total += nums[maxNumPos] * 10
        total += nums[secondMaxNumPos]

    return total


def part_two(inputs):
    total = 0

    for input in inputs:
        nums = list(map(int, list(input)))

        stack = []

        for i in range(len(nums)):
            while stack and len(stack) + (len(nums) - i) > 12 and nums[i] > stack[-1]:
                stack.pop()

            if len(stack) < 12:
                stack.append(nums[i])

        total += int("".join(map(str, stack)))
    return total


def parse_input():
    filename = "input.txt"

    inputs = []

    for line in fileinput.input(files=filename):
        inputs.append(line.rstrip())

    return inputs


if __name__ == "__main__":
    main()
