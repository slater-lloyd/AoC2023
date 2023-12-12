from sys import argv
from itertools import permutations

input = []

inputFile = "day12/test.txt"

if len(argv) == 2:
    inputFile = argv[1]

with open(inputFile) as f:
    input = f.read().splitlines()


def parse(line):
    line = line.split(" ")
    springs = line[0]
    nums = line[1].split(",")
    nums = [int(i) for i in nums]
    return (springs, nums)


def isValidList(springs, nums):
    brokenGrouped = []
    curGroup = ""
    for spring in springs:
        if spring == "#":
            curGroup += "#"
        if len(curGroup) > 0 and spring == ".":
            brokenGrouped.append(curGroup)
            curGroup = ""
    if len(curGroup) > 0:
        brokenGrouped.append(curGroup)

    if len(brokenGrouped) != len(nums):
        return False

    for i in range(len(brokenGrouped)):
        if len(brokenGrouped[i]) != nums[i]:
            return False
    return True


def getAllConfigs(springs, nums):
    totalBroken = sum(nums)
    missingBroken = totalBroken - springs.count("#")
    missingWorking = springs.count("?") - missingBroken
    unknowns = "#"*missingBroken + "."*missingWorking
    
    perms = [p for p in permutations(unknowns)]
    return perms


def part1(springs, nums):
    validsList = []
    for i in range(len(springs)):
        perms = getAllConfigs(springs[i], nums[i])
        countValid = 0
        for perm in perms:
            permList = list(perm)
            permList.reverse()
            temp = [spring if spring != "?" else permList.pop() for spring in springs[i]]
            if isValidList(temp, nums[i]):
                countValid += 1
        validsList.append(countValid)
        print(i, countValid)
    return sum(validsList)

def main():
    springs = []
    nums = []
    for line in input:
        parsed = parse(line)
        springs.append(parsed[0])
        nums.append(parsed[1])

    print("Part 1:", part1(springs, nums))


if __name__ == "__main__":
    main()
