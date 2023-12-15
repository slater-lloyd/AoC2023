from sys import argv

input = []

inputFile = "day15/test.txt"

if len(argv) == 2:
    inputFile = argv[1]

with open(inputFile) as f:
    input = f.read().splitlines()


def parse(line):
    return line.split(",")


def hashStep(step):
    curVal = 0
    for char in step:
        curVal += ord(char)
        curVal *= 17
        curVal = curVal % 256

    return curVal

def part1(steps):
    hashedList = []
    for step in steps:
        hashedList.append(hashStep(step))

    return sum(hashedList)

def part2(steps):
    boxes = {}
    for i in range(256):
        boxes[i] = []
    for step in steps:
        if "-" in step:
            label = step.replace("-", "")
            box = hashStep(label)
            if len(boxes[box]) == 0:
                pass
            elif boxes[box][0][0] == label:
                boxes[box].pop(0)

            for i, _ in enumerate(boxes[box]):
                if boxes[box][i][0] == label:
                    boxes[box].pop(i)
        else:
            lense = step.split("=")
            box = hashStep(lense[0])
            found = False
            for i in range(len(boxes[box])):
                if lense[0] == boxes[box][i][0]:
                    boxes[box][i][1] = lense[1]
                    found = True
            if not found:
                boxes[box].append(lense)

    return calcVals(boxes)

def calcVals(boxes):
    sums = 0
    for boxNum, lenses in boxes.items():
        boxNum = int(boxNum)
        for lenseI in range(len(lenses)):
            val = (boxNum+1) * (lenseI+1) * int(lenses[lenseI][1])
            sums += val
            # print(f"{lenses[lenseI]}: {boxNum+1} * {lenseI+1} * {lenses[lenseI][1]} = {val}")
    return sums


def main():
    print("Part 1:", part1(parse(input[0])))
    print("Part 2:", part2(parse(input[0])))


if __name__ == "__main__":
    main()
