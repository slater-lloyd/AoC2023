from sys import argv

from Brick import Brick
from Grid import Grid

input = []

inputFile = "day22/test.txt"

if len(argv) >= 2:
    inputFile = argv[-1]

with open(inputFile) as f:
    input = f.read().splitlines()


def parse(line):
    line = line.split("~")
    bStart = line[0].split(",")
    bEnd = line[1].split(",")

    for i in range(len(bStart)):
        bStart[i] = int(bStart[i])
        bEnd[i] = int(bEnd[i])
    
    return Brick(bStart, bEnd)

def part1():
    bricks = [parse(line) for line in input]
    r, c, h = 0, 0, 0
    for brick in bricks:
        r = max(r, brick.start[0], brick.end[0])
        c = max(c, brick.start[1], brick.end[1])
        h = max(h, brick.start[2], brick.end[2])
    grid = Grid([[[0 for _ in range(r+1)] for _ in range(c+1)] for _ in range(h+1)])
    
    ind = 1
    for brick in bricks:
        blocks = brick.getAllCoords()
        for block in blocks:
            grid.arr[block.hei][block.col][block.row] = ind
        ind += 1

    for i in range(len(grid.arr[0][0])):
        print(f"  {i}")
        grid.printFace(i)
    for i in range(len(grid.arr[0])):
        print(f"  {i}")
        grid.printFace(i, True)

def part2():
    pass


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
