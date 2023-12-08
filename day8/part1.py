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


def main():
    count = 1
    curInst = "AAA"
    while True:
        for lr in LRCode:
            print(curInst, count)
            if lr == "R":
                curInst = instructions[curInst][1]
            elif lr == "L":
                curInst = instructions[curInst][0]
            else:
                print("ERROR")
                exit(0)
            if curInst == "ZZZ":
                print(count)
                exit(0)
            count += 1
        if curInst == "ZZZ":
            break


if __name__ == "__main__":
    main()
