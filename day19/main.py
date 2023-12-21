from sys import argv

from gear import Gear, Rule, WorkFlow

input = []

inputFile = "day19/test.txt"

if len(argv) >= 2:
    inputFile = argv[-1]

with open(inputFile) as f:
    input = f.read().splitlines()


def parseWorkflow(line):
    line = line.replace("}", "")
    line = line.split("{")
    label = line[0]
    rules = line[1].split(",")
    rulesList = []
    for rule in rules:
        if ":" in rule:
            rule = rule.split(":")
            rulesList.append(Rule(rule[0], rule[1]))
        else:
            rulesList.append(Rule(None, rule))
    
    workFlow = WorkFlow(rulesList)
    return label, workFlow

def parseGear(line):
    line = line.replace("{", "").replace("}", "")
    line = line.split(",")
    vals = []
    for gear in line:
        gear = gear.split("=")
        vals.append(int(gear[1]))
    return Gear(vals[0], vals[1], vals[2], vals[3])

def part1():
    workflows = {}
    gears = []
    breakLine = input.index("")
    for line in input[:breakLine]:
        label, rules = parseWorkflow(line)
        workflows[label] = rules

    for line in input[breakLine+1:]:
        gears.append(parseGear(line))

    aList = []
    rList = []

    for gear in gears:
        curFlow = workflows["in"]
        while True:
            nextLabel = curFlow.process(gear)
            if nextLabel == "A":
                aList.append(gear)
                break
            elif nextLabel == "R":
                rList.append(gear)
                break
            else:
                curFlow = workflows[nextLabel]
    
    sums = [x.sumParts() for x in aList]
    return sum(sums)

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
