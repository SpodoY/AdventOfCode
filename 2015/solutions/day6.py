with open("../inputs/in6.txt") as puzzle_input:
    puzzle_input = [x.rstrip() for x in puzzle_input.readlines()]

# print(puzzle_input)

def analyze_instruction(instruction):
    s = {}
    split = [y.split(',') for y in [x for x in instruction.split(' ')] if len(y.split(',')) == 2]
    s['xc'] = [int(split[0][0]), int(split[1][0])]
    s['yc'] = [int(split[0][1]), int(split[1][1])]
    if 'on' in instruction: s['action'] = 'on'
    if 'off' in instruction: s['action'] = 'off'
    if 'toggle' in instruction: s['action'] = 'toggle'
    return s


def part_one():
    lights = [[-1 for _ in range(1000)] for _ in range(1000)]
    for instruction in puzzle_input:
        infos = analyze_instruction(instruction)
        for col in range(infos['yc'][0], infos['yc'][1] + 1):
            for row in range(infos['xc'][0], infos['xc'][1] + 1):
                if infos['action'] == 'toggle': lights[col][row] *= -1
                if infos['action'] == 'on': lights[col][row] = 1
                if infos['action'] == 'off': lights[col][row] = -1
    print(sum([x.count(1) for x in lights]))


def part_two():
    lights = [[0 for _ in range(1000)] for _ in range(1000)]
    for instruction in puzzle_input:
        infos = analyze_instruction(instruction)
        for col in range(infos['yc'][0], infos['yc'][1] + 1):
            for row in range(infos['xc'][0], infos['xc'][1] + 1):
                if infos['action'] == 'toggle': lights[col][row] += 2
                if infos['action'] == 'on': lights[col][row] += 1
                if infos['action'] == 'off' and lights[col][row] > 0: lights[col][row] -= 1
    print(sum(list(map(sum, lights))))

# part_one()
part_two()