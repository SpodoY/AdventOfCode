import re

with open("../inputs/in5.txt") as puzzle_input:
    puzzle_input = [line.rstrip() for line in puzzle_input.readlines()]


def extractCrates():
    cratesStacks = {}
    for x in range(0, 10): cratesStacks[str(x)] = []
    for x in puzzle_input:
        if '1' in x: break
        for crateIndex in range(0, len(x), 4):
            if x[crateIndex+1] != ' ': cratesStacks[str(crateIndex//4)].append(x[crateIndex+1])
            # print(f'idx: {crateIndex // 4} - {x[crateIndex:crateIndex + 4]}')
    return cratesStacks


def infoFromOp(op):
    return [int(x) for x in re.findall(r'\d+', op)]


def part_one():
    topCrates = ""
    stacks = extractCrates()
    print(f'Stack: {stacks}')
    for instruct in puzzle_input:
        if 'move' in instruct:
            op = infoFromOp(instruct)
            for _ in range(op[0]):
                stacks[str(op[2]-1)].insert(0, stacks[str(op[1]-1)].pop(0))
            # print(f'Stack after: {stacks}')
    for key in stacks.keys():
        try: topCrates += str(stacks[key].pop(0))
        except: pass
    print(topCrates)


def part_two():
    topCrates = ""
    stacks = extractCrates()
    print(f'Stack: {stacks}')
    for instruct in puzzle_input:
        if 'move' in instruct:
            op = infoFromOp(instruct)
            for offset in reversed(range(op[0])):
                stacks[str(op[2] - 1)].insert(0, stacks[str(op[1] - 1)].pop(0 + offset))
    for key in stacks.keys():
        try: topCrates += str(stacks[key].pop(0))
        except: pass
    print(topCrates)


# part_one()
part_two()
# print(puzzle_input)
