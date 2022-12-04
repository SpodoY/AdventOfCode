with open("../inputs/in4.txt") as puzzle_input:
    puzzle_input = [line.rstrip('\n').split(',') for line in puzzle_input.readlines()]


def part_one():
    amount = 0
    for curRange in puzzle_input:
        l_range = [int(x) for x in curRange[0].split('-')]
        r_range = [int(x) for x in curRange[1].split('-')]
        if (l_range[0] <= r_range[0] and l_range[1] >= r_range[1]) or \
                (r_range[0] <= l_range[0] and r_range[1] >= l_range[1]):
            amount += 1
    return amount


def part_two():
    amount = 0
    for curRange in puzzle_input:
        l_range = [int(x) for x in curRange[0].split('-')]
        r_range = [int(x) for x in curRange[1].split('-')]
        rNums = [x for x in range(r_range[0], r_range[1] + 1)]
        for x in range(l_range[0], l_range[1] + 1):
            if x in rNums:
                amount += 1
                break
    return amount


# print(part_one())
print(f'Part 2: {part_two()}')
