import re

with open("inputs/day1.txt") as puzzle_in:
    puzzle_in = [line.rstrip("\n") for line in puzzle_in.readlines()]

sum = 0

units = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for (i, line) in enumerate(puzzle_in):
    findings = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)
    if i == 767: print(i, line, findings)
    first = findings[0] if units.count(findings[0]) == 0 else (units.index(findings[0]) + 1)
    last = findings[-1] if units.count(findings[-1]) == 0 else (units.index(findings[-1]) + 1)
    print(int(str(first) + str(last)))
    sum += int(str(first) + str(last))

print(f'1:2 -> {sum}')