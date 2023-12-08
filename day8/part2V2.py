from math import gcd
input = []


def parse(line):
    line = line.replace(" ", "").replace("(", "").replace(")", "")
    line = line.replace(",", "=").strip()
    return line.split("=")


with open("day8/test.txt", "r") as f:
    input = f.read().splitlines()

LRCode = input[0]
instructions = {}
firstInstruction = parse(input[2])[0]

for line in input[2:]:
    parsed = parse(line)
    instructions[parsed[0]] = (parsed[1], parsed[2])


def part2(startingNode):
    curInst = startingNode
    count = 1
    while True:
        for lr in LRCode:
            if lr == "R":
                curInst = instructions[curInst][1]
            elif lr == "L":
                curInst = instructions[curInst][0]
            else:
                print("ERROR")
                exit(0)
            if curInst[-1] == "Z":
                print(count)
                return count
            count += 1


def main():
    nodes = [inst for inst in instructions.keys() if inst[-1] == "A"]

    sums = []
    for node in nodes:
        print(node)
        sums.append(part2(node))

    lcm = 1
    for i in sums:
        lcm = lcm*i//gcd(lcm, i)
    print(lcm)


if __name__ == "__main__":
    main()
