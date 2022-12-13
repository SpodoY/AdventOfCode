with open("../inputs/testInput.txt") as puzzle_input:
    puzzle_input = [[line.rstrip().split()[0], int(line.rstrip().split()[1])] for line in puzzle_input.readlines()]



print(puzzle_input)