with open("../inputs/in2.txt") as puzzle_input:
    puzzle_input = [[int(num) for num in line.rstrip('\n').split('x')] for line in puzzle_input.readlines()]

sum_wrapping = 0
for paper in puzzle_input:
    l, w, h = paper[0], paper[1], paper[2]
    paper.sort()
    slack = min(l*w, l*h, w*h)
    ribbon = 2 * paper[0] + 2 * paper[1]
    sum_wrapping += l * w * h + ribbon
print(sum_wrapping)