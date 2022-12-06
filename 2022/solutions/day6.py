with open("../inputs/in6.txt") as puzzle_input:
    puzzle_input = puzzle_input.readline()


def solver(msg_length):
    for seq in range(0, len(puzzle_input)):
        if len({*puzzle_input[seq:seq + msg_length]}) == msg_length:
            return seq + msg_length


print(f'Part 1:  {solver(4)}')
print(f'Part 2:  {solver(14)}')