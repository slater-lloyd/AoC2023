from sys import argv

input = []

inputFile = "day14/test.txt"

if len(argv) == 2:
    inputFile = argv[1]

with open(inputFile) as f:
    input = f.read().splitlines()


def parse(line):
    return [x for x in line]


def tilt(platform, direction="north"):
    for rowI in range(len(platform)):
        for colI in range(len(platform[rowI])):
            if platform[rowI][colI] == "O":
                column = [x[colI] for x in platform]
                platform[rowI][colI] = "."
                newRowI = getRolledIndex(column, rowI)
                platform[newRowI][colI] = "O"
    return platform


def getRolledIndex(column, rockIndex):
    column = column[0:rockIndex]
    squareRock = -1
    roundRock = -1
    if "#" in column:
        squareRock = "".join(column).rindex("#")+1
    if "O" in column:
        roundRock = "".join(column).rindex("O")+1

    return max(0, squareRock, roundRock) 


def part1(platform):
    platform = tilt(platform)

    lineSums = []
    for i, line in enumerate(platform):
        lineSums.append((len(platform)-i)*line.count("O"))

    return sum(lineSums)

def main():
    platform = [parse(x) for x in input]
    print("Part 1:", part1(platform))



if __name__ == "__main__":
    main()
