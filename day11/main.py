from sys import argv

input = []

inputFile = "day11/test.txt"

if len(argv) == 2:
    inputFile = argv[1]

with open(inputFile) as f:
    input = f.read().splitlines()

def parse(line):
    return list(line)

def addSpaces(space):
    for line in input:
        space.append(parse(line))
        if "#" not in line:
            space.append(parse(line))

    i = 0
    while i < len(space[0]):
        colVals = [row[i] for row in space]
        if "#" not in colVals:
            for row in space:
                row.insert(i, '.')
            i += 2
        else:
            i += 1

    return space

def isInBounds(loc, space):
    MAX_ROW = len(space)
    MAX_COL = len(space[0])
    if loc[0] < 0 or loc[0] > MAX_ROW:
        print(loc)
        return False
    if loc[1] < 0 or loc[1] > MAX_COL:
        print(loc)
        return False
    return True

def part1(space):
    space = addSpaces(space)
    for line in space:
        print(line)
    galaxyDistances = []
    compared = []
    galaxyLocs = []
    for rowI, row in enumerate(space):
        for colI, col in enumerate(row):
            if col == "#" and (rowI, colI) not in galaxyLocs:
                galaxyLocs.append((rowI, colI))

    for sGalaxy in galaxyLocs:
        compared.append(sGalaxy)
        for dGalaxy in galaxyLocs:
            if dGalaxy not in compared:
                galaxyDistances.append(abs(dGalaxy[0]-sGalaxy[0])+abs(dGalaxy[1]-sGalaxy[1]))
    
    return sum(galaxyDistances)

def addSpacesV2(space):
    rowJumps = []
    colJumps = []
    for lineI, line in enumerate(input):
        space.append(parse(line))
        if "#" not in line:
            rowJumps.append(lineI)
    for i in range(len(space[0])):
        colVals = [row[i] for row in space]
        if "#" not in colVals:
            colJumps.append(i)

    return space, rowJumps, colJumps


def part2(space, gap):
    space, rowJumps, colJumps = addSpacesV2(space)
    for line in space:
        print(line)
    print("rows", rowJumps)
    print("cols", colJumps)
    galaxyDistances = []
    compared = []
    galaxyLocs = []
    for rowI, row in enumerate(space):
        for colI, col in enumerate(row):
            if col == "#" and (rowI, colI) not in galaxyLocs:
                galaxyLocs.append((rowI, colI))

    for sGalaxy in galaxyLocs:
        compared.append(sGalaxy)
        for dGalaxy in galaxyLocs:
            if dGalaxy not in compared:
                dist = abs(dGalaxy[0]-sGalaxy[0])+abs(dGalaxy[1]-sGalaxy[1]) 
                minRow = min(sGalaxy[0], dGalaxy[0])
                maxRow = max(sGalaxy[0], dGalaxy[0])
                minCol = min(sGalaxy[1], dGalaxy[1])
                maxCol = max(sGalaxy[1], dGalaxy[1])
                for row in range(minRow, maxRow):
                    if row in rowJumps:
                        dist += gap
                for col in range(minCol, maxCol):
                    if col in colJumps:
                        dist += gap
                galaxyDistances.append(dist)
    return sum(galaxyDistances)


def main():
    print("Part 1:", part1([]))
    print("Part 2:", part2([], 999999))

if __name__ == "__main__":
    main()
