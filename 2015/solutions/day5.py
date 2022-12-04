with open("../inputs/in5.txt") as puzzle_input:
    puzzle_input = [x.rstrip() for x in puzzle_input.readlines()]

print(puzzle_input)


def part_one():
    niceCount = 0
    for stri in puzzle_input:
        vowels = stri.count('a') + stri.count('e') + stri.count('i') + stri.count('o') + stri.count('u')
        conDouble = False
        bads = stri.count('ab') + stri.count('cd') + stri.count('pq') + stri.count('xy')
        for s in range(len(stri) - 1):
            if stri[s] == stri[s + 1]: conDouble = True
        if vowels >= 3 and conDouble and bads == 0: niceCount += 1
    print(niceCount)


def part_two():
    niceCount = 0
    for stri in puzzle_input:
        aba, dPair = False, False
        for s in range(len(stri) - 1):
            if not dPair and stri.count(stri[s:s+2]) > 1: dPair = True
            try:
                if not aba and (stri[s] == stri[s+2]): aba = True
            except IndexError: break
        if aba and dPair:
            niceCount+=1
    print(niceCount)


part_one()
part_two()