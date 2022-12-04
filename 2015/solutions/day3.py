with open("../inputs/in3.txt") as puzzle_input:
    puzzle_input = puzzle_input.readline()

print(puzzle_input)

x, y = 0, 0
rx, ry = 0, 0
houses = {"0 0"}
for (index, direction) in enumerate(puzzle_input):
    if index % 2 == 0:
        if direction == '^': y += 1
        if direction == 'v': y -= 1
        if direction == '<': x -= 1
        if direction == '>': x += 1
        houses.add(str(x) + ' ' + str(y))
    else:
        if direction == '^': ry += 1
        if direction == 'v': ry -= 1
        if direction == '<': rx -= 1
        if direction == '>': rx += 1
        houses.add(str(rx) + ' ' + str(ry))

print(houses)
print(len(houses))
