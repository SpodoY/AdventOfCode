import hashlib

with open("../inputs/in4.txt") as puzzle_input:
    puzzle_input = puzzle_input.readline()

print(puzzle_input)
hashNum = 1
while True:
    res = hashlib.md5((puzzle_input + str(hashNum)).encode()).hexdigest()
    if res[0:6] == '0':
        print(hashNum)
        break
    hashNum += 1