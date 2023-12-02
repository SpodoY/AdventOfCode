import math
import re

with open("./inputs/day2.txt") as games:
    games = [(line.rstrip("\n").split(":")[0].split(" ")[1], line.rstrip("\n").split(":")[1].split(";"))
             for line in games.readlines()]

max_possible = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def partOne():
    possible_games = []

    for game in games:
        isValid = True
        for draw in game[1]:
            groups = re.findall(r"(\d+) (\w+)", draw)
            for cubes in groups:
                if int(cubes[0]) > max_possible[cubes[1]]: isValid = False
        if isValid: possible_games.append(int(game[0]))
    return possible_games


def partTwo():
    powerOfGame = []
    for game in games:
        gameLowest = {'red': 0, 'green': 0, 'blue': 0}
        for draw in game[1]:
            groups = re.findall(r"(\d+) (\w+)", draw)
            for cubes in groups:
                if int(cubes[0]) > gameLowest[cubes[1]]: gameLowest[cubes[1]] = int(cubes[0])
        powerOfGame.append(math.prod(gameLowest.values()))
    return powerOfGame


print(sum(partOne()))
p2 = partTwo()
print(sum(p2), p2)
