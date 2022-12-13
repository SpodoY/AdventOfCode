with open("../inputs/in1.txt") as puzzle_input:
    puzzle_input = puzzle_input.readline()

# Part One
print(f'Part 1: {puzzle_input.count("(") - puzzle_input.count(")")}')

# Part Two
curFloor = 0
for (index, lvl) in enumerate(puzzle_input):
    if lvl == '(': curFloor += 1
    if lvl == ')': curFloor -= 1
    # print(f'{index+1}: {curFloor}')
    if curFloor == -1: break
    print(index+1)
