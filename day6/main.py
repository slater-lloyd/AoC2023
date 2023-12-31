import math
import time

lines = []

with open("day6/test.txt", "r") as f:
    lines = f.readlines()


def parse(line):
    line = line.split()
    return [int(x) for x in line[1:]]


def getWinnableCount(time, dist):
    count = 0
    while count <= time/2:
        curMethodDistance = count * (time-count)
        if curMethodDistance > dist:
            return time - (count*2) + 1
        count += 1

    return 0


def getWinnableCountV2(time, dist):
    # dist = (totalTime-holdTime) * holdTime
    # dist/(totalTime-holdTime) = holdTime
    # dist/totalTime = holdTime^2
    # holdTime = sqrt(dist/totalTime)
    holdTime = math.floor((time - math.sqrt(time**2 - (4*dist))) / 2)
    holdTime2 = math.ceil((time + math.sqrt(time**2 - (4*dist))) / 2)

    return holdTime2 - holdTime - 1


def main():
    times = parse(lines[0])
    dist = parse(lines[1])

    st = time.time()
    winCounts = []
    for i in range(len(times)):
        winCounts.append(getWinnableCount(times[i], dist[i]))

    product = math.prod(winCounts)

    print(f"Answer V1: {product}")
    print(f"V1 List: {winCounts}")
    print(f"V1 Time: {time.time() - st} seconds")

    st = time.time()

    winCountsV2 = []
    for i in range(len(times)):
        winCountsV2.append(getWinnableCountV2(times[i], dist[i]))

    productV2 = math.prod(winCountsV2)

    print(f"Answer V2: {productV2}")
    print(f"V2 List: {winCountsV2}")
    print(f"V2 Time: {time.time() - st} seconds")


if __name__ == "__main__":
    main()
