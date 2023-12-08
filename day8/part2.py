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
    count = 0
    nodes = [inst for inst in instructions.keys() if inst[-1] == "A"]
    while True:
        print(nodes, count)
        for lr in LRCode:
            count += 1
            for i in range(len(nodes)):
                if lr == "R":
                    nodes[i] = instructions[nodes[i]][1]
                elif lr == "L":
                    nodes[i] = instructions[nodes[i]][0]
                else:
                    print("ERROR")
                    exit(0)
            done = True
            for node in nodes:
                if node[-1] != "Z":
                    done = False
                    break
            if done:
                print(count)
                exit(0)


if __name__ == "__main__":
    main()
