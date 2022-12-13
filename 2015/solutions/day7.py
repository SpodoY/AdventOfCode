with open("../inputs/testInput.txt") as puzzle_input:
    puzzle_input = [x.rstrip() for x in puzzle_input.readlines()]

print(puzzle_input)


def getOp(op):
    opInfo = {}
    infos = op.split(' -> ')
    try:
        opInfo['value'] = int(infos[0])
    except:
        infos[0] = infos[0].split(' ')
    print(infos)
    opInfo['trgt'] = infos[1]
    return opInfo


for op in puzzle_input:
    states = {}
    print(getOp(op))
