from AlmanacLine import AlmanacLine

lines = []
with open("day5/test.txt", "r") as f:
    lines = f.read()
    lines = lines.splitlines()

seedStrings = lines[0].split()
seeds = []
for seed in seedStrings[1:]:
    seeds.append(int(seed))
seedsDict = {}

keysInOrder = []


def parse(line) -> AlmanacLine:
    line = line.split()
    return AlmanacLine(int(line[0]), int(line[1]), int(line[2]))


mapsDict = {}
newCat = False
for line in lines[1:]:
    if line == "":
        curMap = False
    elif not curMap:
        curMap = line
        keysInOrder.append(curMap)
        mapsDict[curMap] = []
    else:
        mapsDict[curMap].append(parse(line))


def getPart2Seeds():
    retList = []
    for i in range(0, len(seeds), 2):
        retList.extend(range(seeds[i], seeds[i]+seeds[i+1], 1000))
    print("Got Seeds")
    return retList


def isInP2Range(num):
    for i in range(0, len(seeds), 2):
        if num >= seeds[i] and num <= seeds[i]+seeds[i+1]:
            return True
    return False


def testSingleSeed(seedNum):
    curVal = seedNum
    for key in keysInOrder:
        for line in mapsDict[key]:
            if line.isInRange(curVal):
                curVal = line.getConverted(curVal)
                break
    return curVal


def main():
    # for seed in getPart2Seeds():
    # curConversion = seed
    # for key in keysInOrder:
    #    for line in mapsDict[key]:
    #        if line.isInRange(curConversion):
    #            curConversion = line.getConverted(curConversion)
    #            break
    # seedsDict[seed] = curConversion

    # print(sorted(list(seedsDict.values()))[0])
    testLocation = 5500000
    curConversion = 0
    while True:
        curConversion = testLocation
        for key in reversed(keysInOrder):
            for line in mapsDict[key]:
                if line.isInDestRange(curConversion):
                    curConversion = line.unConvert(curConversion)
                    break
        if isInP2Range(curConversion):
            print(f"Result: {testLocation} (seed: {curConversion})")
            break
        testLocation += 1
        if testLocation % 10000 == 0:
            print(f"Working on {testLocation}")


if __name__ == "__main__":
    main()
