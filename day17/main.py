import math
from sys import argv

input = []

inputFile = "day17/test.txt"

if len(argv) == 2:
    inputFile = argv[1]

with open(inputFile) as f:
    input = f.read().splitlines()

MAX_ROW = len(input)
MAX_COL = len(input[0])
RIGHT = (0, 1)
LEFT = (0, -1)
UP = (-1, 0)
DOWN = (1, 0)

def parse(line):
    return [int(x) for x in line]

def strMove(move):
    movesDict = {
        UP: "UP",
        DOWN: "DOWN",
        RIGHT: "RIGHT",
        LEFT: "LEFT"
    }
    return movesDict[move]


def isInBounds(loc):
    if loc[0] < 0 or loc[0] >= MAX_ROW:
        return False
    if loc[1] < 0 or loc[1] >= MAX_COL:
        return False
    return True

def dijk_setup():
    sptSet = set()
    dist = {} # loc -> (dist, moves[])
    city = [parse(x) for x in input]

    for rowI, row in enumerate(city):
        for colI, col in enumerate(row):
            dist[(rowI, colI)] = [math.inf, []]

    dist[(0, 0)][0] = 0

    return sptSet, dist, city

def getMinNode(sptSet, dist):
    minKey = None
    minDist = math.inf
    for key in dist.keys():
        if key not in sptSet:
            if dist[key][0] < minDist:
                minKey = key
                minDist = dist[key][0]
    if not minKey:
        print("Error getting min key")
        exit(1)
    return minKey, dist[minKey][1].copy()

def getAdjacents(loc, moves):
    possibleMoves = [UP, DOWN, RIGHT, LEFT]
    if len(moves) == 0:
        pass
    elif moves[-1] == UP:
        possibleMoves.remove(DOWN)
    elif moves[-1] == DOWN:
        possibleMoves.remove(UP)
    elif moves[-1] == RIGHT:
        possibleMoves.remove(LEFT)
    elif moves[-1] == LEFT:
        possibleMoves.remove(RIGHT)

    if len(moves) < 3:
        pass
    elif moves[-3:].count(moves[-1]) == 3:
        print("THREE", moves[-3:])
        possibleMoves.remove(moves[-1])
    
    adjacents = []
    for move in possibleMoves:
        adjacent = (loc[0]+move[0], loc[1]+move[1])
        if isInBounds(adjacent):
            adjacents.append(adjacent)
    return adjacents.copy(), possibleMoves.copy()

def part1():
    sptSet, dist, city = dijk_setup()
    while len(sptSet) != len(dist.keys()):
        curNode, curMoves = getMinNode(sptSet, dist)
        sptSet.add(curNode)
        adjacents, moves = getAdjacents(curNode, curMoves)
        for i in range(len(adjacents)):
            adj = adjacents[i]
            move = moves[i]
            adjWeight = city[adj[0]][adj[1]]
            newWeight = dist[curNode][0] + adjWeight
            if newWeight < dist[adj][0]:
                dist[adj][0] = newWeight
                dist[adj][1] = curMoves.copy()
                dist[adj][1].append(move)
        
    printPath(city, dist[(MAX_ROW-1, MAX_COL-1)][1])
    return dist[(MAX_ROW-1, MAX_COL-1)]

def printPath(city, moves):
    copyCity = city.copy()
    cur = (0, 0)
    for move in moves[6:]:
        copyCity[cur[0]][cur[1]] = "X"
        cur = (cur[0]+move[0], cur[1]+move[1])

    for line in copyCity:
        print(line)

def main():
    print("Part 1:", part1())


if __name__ == "__main__":
    main()
