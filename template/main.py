from sys import argv

input = []

inputFile = "test.txt"

if len(argv) == 2:
    inputFile = argv[1]

with open(inputFile) as f:
    input = f.read().splitlines()


def parse(line):
    return line


def main():
    pass


if __name__ == "__main__":
    main()
