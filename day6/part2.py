import math

lines = []

with open("day6/test.txt", "r") as f:
    lines = f.read()
    lines.replace(" ", "")
    lines = lines.splitlines()


def parse(line):
    line = line.replace(" ", "").split(":")
    return [int(line[1])]


def getWinnableCount(time, dist):
    count = 0
    while count <= time/2:
        curMethodDistance = count * (time-count)
        if curMethodDistance > dist:
            return time - (count*2) + 1
        count += 1

    return 0


def main():
    times = parse(lines[0])
    dist = parse(lines[1])

    winCounts = []
    for i in range(len(times)):
        winCounts.append(getWinnableCount(times[i], dist[i]))

    product = math.prod(winCounts)

    print(f"Answer: {product}")
    print(winCounts)


if __name__ == "__main__":
    main()
