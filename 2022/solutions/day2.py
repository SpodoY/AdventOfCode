A = 'ROCK'
B = 'PAPER'
C = 'SCISSOR'
X = 'ROCK'
Y = 'PAPER'
Z = 'SCISSOR'

with open("../inputs/in2.txt") as puzzle_input:
    puzzle_input = [line.rstrip('\n').split(' ') for line in puzzle_input.readlines()]


def part_one():
    score = 0
    for ins in puzzle_input:
        if ins[0] == 'A':
            if ins[1] == 'X': score += 4
            if ins[1] == 'Y': score += 8
            if ins[1] == 'Z': score += 3
        if ins[0] == 'B':
            if ins[1] == 'X': score += 1
            if ins[1] == 'Y': score += 5
            if ins[1] == 'Z': score += 9
        if ins[0] == 'C':
            if ins[1] == 'X': score += 7
            if ins[1] == 'Y': score += 2
            if ins[1] == 'Z': score += 6
    print(score)


# X -> Lose
# Y -> Draw
# Z -> Win

def part_two():
    score = 0
    for ins in puzzle_input:
        if ins[0] == 'A':
            if ins[1] == 'X': score += 3
            if ins[1] == 'Y': score += 4
            if ins[1] == 'Z': score += 8
        if ins[0] == 'B':
            if ins[1] == 'X': score += 1
            if ins[1] == 'Y': score += 5
            if ins[1] == 'Z': score += 9
        if ins[0] == 'C':
            if ins[1] == 'X': score += 2
            if ins[1] == 'Y': score += 6
            if ins[1] == 'Z': score += 7
    print(score)


part_two()
