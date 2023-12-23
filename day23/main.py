from sys import argv

input = []

inputFile = "dayX/test.txt"

if len(argv) >= 2:
    inputFile = argv[-1]

with open(inputFile) as f:
    input = f.read().splitlines()


def parse(line):
    return line

def part1():
    pass

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
