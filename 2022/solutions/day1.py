import numpy as np

with open("../inputs/testInput.txt") as puzzle_input:
    puzzle_input = [line.rstrip('\n') for line in puzzle_input.readlines()]

max_snacks_elfes = []
curMax = 0
for capacity in puzzle_input:
    if capacity == '':
        max_snacks_elfes.append(curMax)
        curMax = 0
        continue
    curMax += int(capacity)
    print(capacity)


max_snacks_elfes = np.sort(max_snacks_elfes)

print(max_snacks_elfes)
# print(max_snacks_elfes[-1])
# print(max_snacks_elfes[-2])
# print(max_snacks_elfes[-3])

print(max_snacks_elfes[-1] + max_snacks_elfes[-2] + max_snacks_elfes[-3])