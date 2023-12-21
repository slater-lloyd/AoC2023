from sys import argv

input = []

inputFile = "day18/test.txt"

if len(argv) >= 2:
    inputFile = argv[-1]

with open(inputFile) as f:
    input = f.read().splitlines()


def parse(line):
    line = line.split()
    return [line[0], int(line[1]), line[2]]

def parseV2(line):
    line = line.split()
    hexVals = line[2][2:-1]
    direction = hexVals[-1]
    intNum = int(hexVals[:-1], 16)
    direction = hexVals[-1]
    if direction == "0":
        direction = "R"
    elif direction == "1":
        direction = "D"
    elif direction == "2":
        direction = "L"
    elif direction == "3":
        direction = "U"
    else:
        print("ERROR IN PARSING")
    return [direction, intNum].copy()

def part1():
    codes = [parse(line) for line in input]
    Rs = sum([x[1] for x in codes if x[0] == "R"])
    Ls = sum([x[1] for x in codes if x[0] == "L"])
    Us = sum([x[1] for x in codes if x[0] == "U"])
    Ds = sum([x[1] for x in codes if x[0] == "D"])

    area = [[0]*(Rs+Ls)*2 for _ in range((Us+Ds)*2)]
    
    cur = [Rs+Ls, Us+Ds]
    area[cur[0]][cur[1]] = "X"
    for code in codes:
        if code[0] == "R":
            for _ in range(code[1]):
                cur[1] += 1 
                area[cur[0]][cur[1]] = "X"
        if code[0] == "L":
            for _ in range(code[1]):
                cur[1] -= 1 
                area[cur[0]][cur[1]] = "X"
        if code[0] == "U":
            for _ in range(code[1]):
                cur[0] -= 1 
                area[cur[0]][cur[1]] = "X"
        if code[0] == "D":
            for _ in range(code[1]):
                cur[0] += 1 
                area[cur[0]][cur[1]] = "X"

    return calcArea(area)

def calcArea(shape):
    count = 0
    shape = floodFill(shape, len(shape), len(shape[0]), 0, 0, 0, 1)
    for row in shape:
        count += row.count(0) + row.count("X")
    return count

def isValid(screen, m, n, x, y, prevC, newC):
    if x<0 or x>= m\
       or y<0 or y>= n or\
       screen[x][y]!= prevC\
       or screen[x][y]== newC:
        return False
    return True
 
 
# FloodFill function
def floodFill(screen,  
            m, n, x,  
            y, prevC, newC):
    queue = []
     
    # Append the position of starting 
    # pixel of the component
    queue.append([x, y])
 
    # Color the pixel with the new color
    screen[x][y] = newC
 
    # While the queue is not empty i.e. the 
    # whole component having prevC color 
    # is not colored with newC color
    while queue:
         
        # Dequeue the front node
        currPixel = queue.pop()
         
        posX = currPixel[0]
        posY = currPixel[1]
         
        # Check if the adjacent
        # pixels are valid
        if isValid(screen, m, n,  
                posX + 1, posY,  
                        prevC, newC):
             
            # Color with newC
            # if valid and enqueue
            screen[posX + 1][posY] = newC
            queue.append([posX + 1, posY])
         
        if isValid(screen, m, n,  
                    posX-1, posY,  
                        prevC, newC):
            screen[posX-1][posY]= newC
            queue.append([posX-1, posY])
         
        if isValid(screen, m, n,  
                posX, posY + 1,  
                        prevC, newC):
            screen[posX][posY + 1]= newC
            queue.append([posX, posY + 1])
         
        if isValid(screen, m, n,  
                    posX, posY-1,  
                        prevC, newC):
            screen[posX][posY-1]= newC
            queue.append([posX, posY-1])
    return screen

def getPoints(codes):
    coords = []
    curCoord = [0, 0]
    parim = 0
    for code in codes:
        if code[0] == "R":
            curCoord[0] += code[1]
            parim += code[1]
        elif code[0] == "L":
            curCoord[0] -= code[1]
            parim += code[1]
        elif code[0] == "U":
            curCoord[1] += code[1]
            parim += code[1]
        elif code[0] == "D":
            curCoord[1] -= code[1]
            parim += code[1]
        else:
            print("ERROR IN POINTS")
        coords.append(curCoord.copy())
    return coords, parim

def getShoelace(coords):
    coordCount = len(coords)
    leftProd = 0
    rightProd = 0
    for i in range(coordCount):
        leftProd += coords[i][0] * coords[(i+1)%coordCount][1]
    for i in range(coordCount):
        rightProd += coords[(i+1)%coordCount][0] * coords[i][1]
    return abs(leftProd-rightProd)/2


def part2():
    codes = [parseV2(line) for line in input]
    points, parim = getPoints(codes)
    return getShoelace(points) + parim/2 + 1


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
