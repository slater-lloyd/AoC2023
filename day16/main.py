import enum
from sys import argv

input = []

inputFile = "day16/test.txt"

tileDirections = {}

RIGHT = (0, 1)
LEFT = (0, -1)
UP = (-1, 0)
DOWN = (1, 0)

if len(argv) == 2:
    inputFile = argv[1]

with open(inputFile) as f:
    input = f.read().splitlines()

MAX_ROW = len(input)
MAX_COL = len(input[0])


def parse(line):
    return [x for x in line]


def energize(plane, tile, direction):
    if direction in tileDirections[tile]:
        return
    while True:
        tileDirections[tile].append(direction)
        tileSymbol = plane[tile[0]][tile[1]]
        if tileSymbol == "." or (direction in [RIGHT, LEFT] and tileSymbol == "-") or (direction in [UP, DOWN] and tileSymbol == "|"):
            newTile = tile[0]+direction[0], tile[1]+direction[1]
            if isInBounds(newTile, plane):
                tile = newTile
            else:
                return
        elif tileSymbol == "/":
            if direction == RIGHT:
                direction = UP
            elif direction == UP:
                direction = RIGHT
            elif direction == LEFT:
                direction = DOWN
            elif direction == DOWN:
                direction = LEFT
            newTile = tile[0]+direction[0], tile[1]+direction[1]
            if isInBounds(newTile, plane):
                tile = newTile
            else:
                return
        elif tileSymbol == "\\":
            if direction == RIGHT:
                direction = DOWN
            elif direction == UP:
                direction = LEFT
            elif direction == LEFT:
                direction = UP
            elif direction == DOWN:
                direction = RIGHT
            newTile = tile[0]+direction[0], tile[1]+direction[1]
            if isInBounds(newTile, plane):
                tile = newTile
            else:
                return
        elif tileSymbol == "|" and direction in [RIGHT, LEFT]:
            direction = UP
            newTile = tile[0]+direction[0], tile[1]+direction[1]
            if isInBounds(newTile, plane):
                energize(plane, newTile, direction)
            direction = DOWN
            newTile = tile[0]+direction[0], tile[1]+direction[1]
            if isInBounds(newTile, plane):
                energize(plane, newTile, direction)
            return
        elif tileSymbol == "-" and direction in [UP, DOWN]:
            direction = RIGHT
            newTile = tile[0]+direction[0], tile[1]+direction[1]
            if isInBounds(newTile, plane):
                energize(plane, newTile, direction)
            direction = LEFT
            newTile = tile[0]+direction[0], tile[1]+direction[1]
            if isInBounds(newTile, plane):
                energize(plane, newTile, direction)
            return


def isInBounds(loc, space):
    if loc[0] < 0 or loc[0] >= MAX_ROW:
        return False
    if loc[1] < 0 or loc[1] >= MAX_COL:
        return False
    return True

        
def part1(plane):
    energize(plane, (0, 0), RIGHT)
    return sum(1 for y in tileDirections.values() if len(y)>0)

def part2(plane):
    maxes = []
    for rowI, row in enumerate(plane):
        for colI, col in enumerate(row):
            if rowI == 0:
                energize(plane, (rowI, colI), DOWN)
                maxes.append(sum(1 for y in tileDirections.values() if len(y)>0)) 
                resetTileDirections()
            elif rowI == MAX_ROW-1:
                energize(plane, (rowI, colI), UP)
                maxes.append(sum(1 for y in tileDirections.values() if len(y)>0)) 
                resetTileDirections()
            elif colI == 0:
                energize(plane, (rowI, colI), RIGHT)
                maxes.append(sum(1 for y in tileDirections.values() if len(y)>0)) 
                resetTileDirections()
            elif colI == MAX_COL-1:
                energize(plane, (rowI, colI), LEFT)
                maxes.append(sum(1 for y in tileDirections.values() if len(y)>0)) 
                resetTileDirections()
                
    return max(maxes)

def resetTileDirections():
    for rowI, row in enumerate(input):
        for colI, col in enumerate(row):
            tileDirections[(rowI, colI)] = []


def main():
    resetTileDirections()
    plane = [parse(line) for line in input]

    print("Part 1:", part1(plane))
    resetTileDirections()
    print("Part 2:", part2(plane))


if __name__ == "__main__":
    main()
