from sys import argv


input = []

inputFile = "day21/test.txt"

if len(argv) >= 2:
    inputFile = argv[-1]

with open(inputFile) as f:
    input = f.read().splitlines()


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
    return line

def part1():
    garden = input.copy()
    start = [0, 0]
    for rowI, row in enumerate(garden):
        for colI, col in enumerate(row):
            if col == "S":
                start = [rowI, colI]
                break

    possiblePlots = set()
    possiblePlots.add(tuple(start))
    for _ in range(64):
        nextPlots = []
        for plot in possiblePlots:
            nextPlots.extend(getNext(garden, plot))

        possiblePlots = set(tuple(i) for i in nextPlots)

    return len(possiblePlots)

def getNext(garden, plot):
    nextPlots = []

    dirs = [UP, DOWN, RIGHT, LEFT]

    for dir in dirs:
        loc = [plot[0]+dir[0], plot[1]+dir[1]]
        if isInBounds(loc):
            if garden[loc[0]][loc[1]] != "#":
                nextPlots.append(loc)

    return nextPlots


def part2():
    garden = input.copy()
    start = [0, 0]
    for rowI, row in enumerate(garden):
        for colI, col in enumerate(row):
            if col == "S":
                start = [rowI, colI]
                break

    
    touching = []
    for rowI, row in enumerate(garden):
        for colI, col in enumerate(row):
            if col == "S" or col == ".":
                touching.append(getInboundsCount(garden, [rowI, colI]))

    avgTouch = sum(touching)/len(touching)
    val = 0
    for i in range(26501365):
        val += avgTouch * i
    return val

def getNextV2(garden, plot):
    nextPlots = []

    dirs = [UP, DOWN, RIGHT, LEFT]

    for dir in dirs:
        loc = [(plot[0]+dir[0])%MAX_ROW, (plot[1]+dir[1])%MAX_COL]
        if garden[loc[0]][loc[1]] != "#":
            nextPlots.append(loc)

    return nextPlots

def getInboundsCount(garden, plot):
    nextPlots = []

    dirs = [UP, DOWN, RIGHT, LEFT]

    for dir in dirs:
        loc = [(plot[0]+dir[0])%MAX_ROW, (plot[1]+dir[1])%MAX_COL]
        if garden[loc[0]][loc[1]] != "#":
            nextPlots.append(loc)

    return len(nextPlots)

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
