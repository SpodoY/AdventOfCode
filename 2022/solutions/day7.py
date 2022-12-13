with open("../inputs/in7.txt") as puzzle_input:
    puzzle_input = [line.rstrip() for line in puzzle_input.readlines()]

dirSizes, curPath = {}, []
for command in puzzle_input:
    if command.startswith("$ cd"):
        newDir = command.split()[2]
        if newDir == "/":
            curPath.append("/")
        elif newDir == "..":
            last = curPath.pop()
        else:
            curPath.append(f"{curPath[-1]}{'/' if curPath[-1] != '/' else ''}{newDir}")
    if command[0].isnumeric():
        for dirs in curPath:
            dirSizes.setdefault(dirs, 0)
            dirSizes[dirs] += int(command.split()[0])


print(f"Part 1: {sum(s for s in dirSizes.values() if s <= 100_000)}")
print(f"Part 2: {min(s for s in dirSizes.values() if s >= 30_000_000 - (70_000_000 - dirSizes['/']))}")
