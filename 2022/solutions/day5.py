import re

with open("../inputs/in5.txt") as puzzle_input:
    puzzle_input = [line.rstrip() for line in puzzle_input.readlines()]


def extractCrates():
    cratesStacks = {}
    for x in puzzle_input:
        if '1' in x: break
        for crateIndex in range(0, len(x), 4):
            if x[crateIndex+1] != ' ':
                cratesStacks.setdefault(str(crateIndex//4), [])
                cratesStacks[str(crateIndex//4)].append(x[crateIndex+1])
    return cratesStacks


def infoFromOp(op):
    return [int(x) for x in re.findall(r"\d+", op)]


def solver(part2):
    topCrates = ""
    stacks = extractCrates()
    for instruct in puzzle_input:
        if 'move' in instruct:
            op = infoFromOp(instruct)
            if not part2:
                for _ in range(op[0]):
                    stacks[str(op[2]-1)].insert(0, stacks[str(op[1]-1)].pop(0))
            else:
                for offset in reversed(range(op[0])):
                    stacks[str(op[2] - 1)].insert(0, stacks[str(op[1] - 1)].pop(0 + offset))
    for key in sorted(stacks.keys()):
        topCrates += str(stacks[key].pop(0))
    print(topCrates)


solver(False)