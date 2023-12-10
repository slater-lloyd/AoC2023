from sys import argv
import re

input = []

inputFile = "day10/test.txt"
if len(argv) == 2:
    inputFile = argv[1]

with open(inputFile, "r") as f:
    input = f.read().splitlines()

MAX_ROW = len(input)-1
MAX_COL = len(input[0])-1
UP_LIST = ["7", "|", "F", "S"]
DOWN_LIST = ["J", "|", "L", "S"]
LEFT_LIST = ["F", "-", "L", "S"]
RIGHT_LIST = ["7", "-", "J", "S"]


def findFirstMove(row, col):
    if isInBounds((row-1, col)):
        if input[row-1][col] in UP_LIST:
            return (row-1, col)
    if isInBounds((row+1, col)):
        if input[row+1][col] in DOWN_LIST:
            return (row+1, col)
    if isInBounds((row, col-1)):
        if input[row][col-1] in LEFT_LIST:
            return (row, col-1)
    if isInBounds((row, col+1)):
        if input[row][col+1] in RIGHT_LIST:
            return (row, col+1)
    print(f"Error: ({row}, {col}) ({input[row][col]})")


def findS():
    for row, line in enumerate(input):
        for col, pipe in enumerate(line):
            if pipe == "S":
                return (row, col)


def isInBounds(loc):
    if loc[0] < 0 or loc[0] > MAX_ROW:
        print(loc)
        return False
    if loc[1] < 0 or loc[1] > MAX_COL:
        print(loc)
        return False
    return True


def findNextMove(curLoc, prevLoc):
    curType = input[curLoc[0]][curLoc[1]]
    up = (curLoc[0]-1, curLoc[1])
    down = (curLoc[0]+1, curLoc[1])
    right = (curLoc[0], curLoc[1]+1)
    left = (curLoc[0], curLoc[1]-1)

    if curType == "-":
        up = None
        down = None
    elif curType == "|":
        right = None
        left = None
    elif curType == "J":
        right = None
        down = None
    elif curType == "L":
        left = None
        down = None
    elif curType == "7":
        right = None
        up = None
    elif curType == "F":
        left = None
        up = None

    if up and up != prevLoc and isInBounds(up):
        if input[up[0]][up[1]] in UP_LIST:
            return up
    if down and down != prevLoc and isInBounds(down):
        if input[down[0]][down[1]] in DOWN_LIST:
            return down
    if right and right != prevLoc and isInBounds(right):
        if input[right[0]][right[1]] in RIGHT_LIST:
            return right
    if left and left != prevLoc and isInBounds(left):
        if input[left[0]][left[1]] in LEFT_LIST:
            return left
    print(isInBounds(right))
    print(f"Error: ({curLoc[0]}, {curLoc[1]}) ({input[curLoc[0]][curLoc[1]]})")


def part1(newPipe=None):
    sLoc = findS()

    prevLoc = sLoc
    curLoc = findFirstMove(sLoc[0], sLoc[1])
    if newPipe:
        newPipe[sLoc[0]][sLoc[1]] = input[sLoc[0]][sLoc[1]]

    count = 0
    while True:
        if newPipe:
            newPipe[curLoc[0]][curLoc[1]] = input[curLoc[0]][curLoc[1]]
        tempLoc = curLoc
        curLoc = findNextMove(curLoc, prevLoc)
        prevLoc = tempLoc
        count += 1
        if curLoc == sLoc:
            if newPipe:
                return newPipe
            return (count+1)/2


def replaceS(map):
    sLoc = findS()
    possibleVals = ["-", "|", "L", "J", "F", "7"]

    curLoc = sLoc
    up = (curLoc[0]-1, curLoc[1])
    down = (curLoc[0]+1, curLoc[1])
    right = (curLoc[0], curLoc[1]+1)
    left = (curLoc[0], curLoc[1]-1)

    if isInBounds(up):
        if map[up[0]][up[1]] in UP_LIST:
            if "-" in possibleVals:
                possibleVals.remove("-")
            if "F" in possibleVals:
                possibleVals.remove("F")
            if "7" in possibleVals:
                possibleVals.remove("7")
    if isInBounds(down):
        if map[down[0]][down[1]] in DOWN_LIST:
            if "-" in possibleVals:
                possibleVals.remove("-")
            if "J" in possibleVals:
                possibleVals.remove("J")
            if "L" in possibleVals:
                possibleVals.remove("L")
    if isInBounds(right):
        if map[right[0]][right[1]] in RIGHT_LIST:
            if "|" in possibleVals:
                possibleVals.remove("|")
            if "J" in possibleVals:
                possibleVals.remove("J")
            if "7" in possibleVals:
                possibleVals.remove("7")
    if isInBounds(left):
        if map[left[0]][left[1]] in LEFT_LIST:
            if "|" in possibleVals:
                possibleVals.remove("|")
            if "F" in possibleVals:
                possibleVals.remove("F")
            if "L" in possibleVals:
                possibleVals.remove("L")
    if len(possibleVals) > 1:
        print("Could not determine S val")
        exit(1)
    map[sLoc[0]][sLoc[1]] = possibleVals[0]
    return map


def isInside(pipeMap, loc):
    rowVal = "".join(pipeMap[loc[0]][0:loc[1]])
    colVal = pipeMap[loc[0]][loc[1]]
    rowVal = rowVal.replace(".", "").replace("I", "").replace("-", "")
    count = 0
    if colVal == ".":
        rowVal = re.sub(r'F-*7', "", rowVal)
        rowVal = re.sub(r'L-*J', "", rowVal)
        rowVal = re.sub(r'\|\|', "", rowVal)
        count += rowVal.count("FJ")
        count += rowVal.count("L7")
        count += rowVal.count("|")
    if count % 2 != 0:
        print(rowVal)
        return True
    return False


def part2():
    # Create new pipe map with only real loop and dots
    pipeOnly = [["."]*(MAX_COL+1) for i in range(MAX_ROW+1)]
    pipeOnly = part1(pipeOnly)
    pipeOnly = replaceS(pipeOnly)
    # for each dot, count barriers in each direction:
    count = 0
    for rowI, rowVal in enumerate(pipeOnly):
        for colI, colVal in enumerate(rowVal):
            if isInside(pipeOnly, (rowI, colI)):
                count += 1
                pipeOnly[rowI][colI] = "I"
    for line in pipeOnly:
        print("".join(line))

    # ||, F7, --, LJ, J7, LF cancel out depending on direction
    # Odd barriers means inside, even means outside
    return count


def main():
    print("Part 1:", part1())
    print("Part 2:", part2())


if __name__ == "__main__":
    main()
