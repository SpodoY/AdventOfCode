from math import prod

with open("../inputs/in8.txt") as puzzle_input:
    puzzle_input = [list(map(int, line.rstrip())) for line in puzzle_input.readlines()]
print(puzzle_input)
forest_length = len(puzzle_input)


def three_dimensional_array(rows, columns, element_size):
    return [[[0 for _ in range(element_size)] for _ in range(columns)] for _ in range(rows)]


def part_one():
    forest_size = forest_length * forest_length
    uncertain_size = (forest_length - 2) * (forest_length - 2)
    visibles = forest_size - uncertain_size
    for y in range(1, forest_length - 1):
        for x in range(1, forest_length - 1):
            up = max(col[x] for col in puzzle_input[:y])
            down = max(col[x] for col in puzzle_input[y + 1:])
            left = max(puzzle_input[y][:x])
            right = max(puzzle_input[y][x + 1:])
            if any(puzzle_input[y][x] > direction for direction in [up, down, left, right]):
                visibles += 1
    print(visibles)


def part_two():
    scenic_scores = [[[int() for _ in range(4)] for _ in range(forest_length - 2)] for _ in range(forest_length - 2)]
    for y in range(1, forest_length - 1):
        for x in range(1, forest_length - 1):
            curPos = puzzle_input[x][y]
            up = list(reversed([col[y] for col in puzzle_input[:x]]))
            down = [col[y] for col in puzzle_input[x + 1:]]
            left = list(reversed(puzzle_input[x][:y]))
            right = puzzle_input[x][y + 1:]

            for index, direction in enumerate([up, left, down, right]):
                cur_bool = [curPos > el for el in direction]
                scenic_scores[y-1][x-1][index] = cur_bool

            # print(f'Up: {up} Down: {down} Left: {left} Right: {right}')
    scores = []
    for x in range(len(scenic_scores)):
        scores.extend(height_score(scenic_scores[y][x]) for y in range(len(scenic_scores)))
    return max(scores)


def height_score(entry):
    scores = []
    for x in entry:
        try:
            score = x.index(False) + 1
            scores.append(score)
        except ValueError:
            score = sum(x)
            scores.append(score)
    # print(scores)
    return prod(scores)

# part_one()
print(part_two())
