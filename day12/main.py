from sys import argv

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

validDict = {}

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

def dnc(springs, nums):
    qIndex = -1
    try:
        qIndex = springs.index("?")
    except ValueError:
        pass
    if qIndex >= 0:
        broken = springs[0:qIndex] + "#" + springs[qIndex+1:]
        working = springs[0:qIndex] + "." + springs[qIndex+1:]
        
        if broken.count("#") <= sum(nums):
            return dnc(broken, nums) + dnc(working, nums)
        else:
            working = working.replace("?", ".")
            if isValidList(working, nums):
                return 1 
            return 0
    else:
        if isValidList(springs, nums):
            return 1 
        return 0

def part1(springs, nums):
    validsList = []
    for i in range(len(springs)):
        countValid = dnc(springs[i], nums[i])
        validsList.append(countValid)

    return sum(validsList)

def part2(springs, nums):
    validsList = []
    for i in range(len(springs)):
        if springs[i][0] != "?" and springs[i][-1] != "?":
            countValid = dnc(springs[i], nums[i])
            print(springs[i], nums[i], countValid)
            validsList.append(countValid)
        else:
            springsX5 = []
            numsX5 = []
            for _ in range(5):
                numsX5.extend(nums[i])
                springsX5.append(springs[i])
            springsX5 = "?".join(springsX5)
            countValid = dnc(springsX5, numsX5)
            print(springsX5, numsX5, countValid)
            validsList.append(countValid)
    return sum(validsList)

def main():
    springs = []
    nums = []
    for line in input:
        parsed = parse(line)
        springs.append(parsed[0])
        nums.append(parsed[1])

    print("Part 1:", part1(springs, nums))
    #print("Part 2:", part2(springs, nums))


if __name__ == "__main__":
    main()
