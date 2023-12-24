from sys import argv
from copy import deepcopy

input = []

inputFile = "day23/test.txt"

if len(argv) >= 2:
    inputFile = argv[-1]

with open(inputFile) as f:
    input = f.read().splitlines()

endCoord = (len(input)-1, input[-1].find("."))

MAX_ROW = len(input)
MAX_COL = len(input[0])
RIGHT = (0, 1)
LEFT = (0, -1)
UP = (-1, 0)
DOWN = (1, 0)

def isInBounds(loc):
    if loc[0] < 0 or loc[0] >= MAX_ROW:
        return False
    if loc[1] < 0 or loc[1] >= MAX_COL:
        return False
    return True

def parse(line):
    return list(line)

def part1():
    map = [parse(line) for line in input]
    startCol = map[0].index(".")
    longest = getLongest(0, startCol, deepcopy(map))
    return longest

def getLongest(row, col, map):
    curDist = 0
    while (row, col) != endCoord:
        curSym = map[row][col]
        map[row][col] = "O"
        curDist += 1
        if curSym == ">":
            col += 1 
        elif curSym == "<":
            col -= 1 
        elif curSym == "v":
            row += 1 
        elif curSym == "^":
            row -= 1
        else:
            nextLocs = getNext(row, col, map)
            if len(nextLocs) == 1:
                row = nextLocs[0][0]
                col = nextLocs[0][1]
            elif len(nextLocs) > 1:
                dists = []
                for loc in nextLocs:
                    dists.append(getLongest(loc[0], loc[1], deepcopy(map)))
                return curDist + max(dists)
            else:
                return 0

    return curDist


def getNext(row, col, map):
    nextPlots = []

    dirs = [UP, DOWN, RIGHT, LEFT]

    for dir in dirs:
        loc = [row+dir[0], col+dir[1]]
        if isInBounds(loc):
            sym = map[loc[0]][loc[1]]
            allowedSyms = ["."]
            if dir == UP:
                allowedSyms.append("^")
            elif dir == DOWN:
                allowedSyms.append("v")
            elif dir == RIGHT:
                allowedSyms.append(">")
            elif dir == LEFT:
                allowedSyms.append("<")
                
            if sym in allowedSyms:
                nextPlots.append(loc)

    return nextPlots


def part2():
    map = [parse(line) for line in input]
    for rowI, row in enumerate(map):
        for colI, col in enumerate(row):
            if col in ["<", ">", "v", "^"]:
                map[rowI][colI] = "."
    startCol = map[0].index(".")
    longest = getLongestV2(0, startCol, deepcopy(map))
    return longest


def getLongestV2(row, col, map):
    curDist = 0
    while (row, col) != endCoord:
        map[row][col] = "O"
        curDist += 1
        nextLocs = getNextV2(row, col, map)
        if len(nextLocs) == 1:
            row = nextLocs[0][0]
            col = nextLocs[0][1]
        elif len(nextLocs) > 1:
            dists = []
            for loc in nextLocs:
                dists.append(getLongestV2(loc[0], loc[1], deepcopy(map)))
            return curDist + max(dists)
        else:
            return 0

    return curDist

def getNextV2(row, col, map):
    nextPlots = []

    dirs = [UP, DOWN, RIGHT, LEFT]

    for dir in dirs:
        loc = [row+dir[0], col+dir[1]]
        if isInBounds(loc):
            sym = map[loc[0]][loc[1]]
            allowedSyms = ["."]

            if sym in allowedSyms:
                nextPlots.append(loc)

    return nextPlots

def main():
    if "-p1" in argv:
        print("Part 1:", part1())
    elif "-p2" in argv:
        print("Part 2:", part2())
    else:
        print("Part 1:", part1())
        print("Part 2:", part2())


if __name__ == "__main__":
    main()
