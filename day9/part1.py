input = []


def parse(line):
    strLine = line.split()
    return [int(val) for val in strLine]


with open("day9/test.txt", "r") as f:
    input = f.read().splitlines()


def getProjection(line):
    newVal = 0
    endVals = []
    endVals.append(line[-1])

    tempLine = line
    while True:
        for i in range(len(tempLine)-1):
            tempLine[i] = tempLine[i+1]-tempLine[i]
        tempLine = tempLine[0:-1]
        if tempLine.count(0) == len(tempLine):
            break
        endVals.append(tempLine[-1])

    endVals.reverse()
    for end in endVals:
        newVal += end

    return newVal


def part1(lines):
    sum = 0
    for line in lines:
        sum += getProjection(line)
    return sum


def getFrontProjection(line):
    newVal = 0
    startVals = []
    startVals.append(line[0])

    tempLine = line.copy()
    while True:
        for i in range(len(tempLine)-1):
            tempLine[i] = tempLine[i+1]-tempLine[i]
        tempLine.pop()
        if tempLine.count(0) == len(tempLine):
            break
        startVals.append(tempLine[0])

    startVals.reverse()
    for start in startVals:
        newVal = start - newVal
    return newVal


def part2(lines):
    sum = 0
    for line in lines:
        sum += getFrontProjection(line)
    return sum


def main():
    lines = [parse(line) for line in input]

    print(f"Part 1: {part1(lines.copy())}")

    lines = [parse(line) for line in input]
    print(f"Part 2: {part2(lines.copy())}")


if __name__ == "__main__":
    main()
