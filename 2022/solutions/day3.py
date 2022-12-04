with open("../inputs/in3.txt") as puzzle_input:
    puzzle_input = [line.rstrip('\n') for line in puzzle_input.readlines()]

def get_value_of_items(dupes, sum):
    for dupe in dupes:
        if ord(dupe) > 96: sum += (ord(dupe) - ord('a') + 1)
        else: sum += (ord(dupe) - ord('A') + 1 + 26)
    return sum

def part_one():
    dupes = []
    sum = 0
    for rucksack in puzzle_input:
        firstPart = rucksack[:len(rucksack) // 2]
        secondPart = rucksack[len(rucksack) // 2:]
        dupes.append(set([i for i in rucksack if firstPart.count(i) > 0 and secondPart.count(i) > 0]).pop())
    print(get_value_of_items(dupes, sum))

def part_two():
    dupes = []
    sum = 0
    for triples_index in range(0, len(puzzle_input), 3):
        r1 = puzzle_input[triples_index]
        r2 = puzzle_input[triples_index + 1]
        r3 = puzzle_input[triples_index + 2]
        dupes.append(set([i for i in r1 + r2 + r3 if r1.count(i) > 0 and r2.count(i) > 0 and r3.count(i) > 0]).pop())
    print(get_value_of_items(dupes, sum))


part_one()
part_two()
