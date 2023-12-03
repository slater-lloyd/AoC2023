inputList = []
with open("test.txt", "r") as f:
    for line in f.readlines():
        inputList.append(line.strip())
maxLineIndex = len(inputList[0])-1
chars = ["=", "@", "#", "$", "%", "-", "&", "*", "/", "+"]


def isSymbol(char):
    if char in chars:
        return True
    return False


def hasAdjacentSymbol(start, end, line):
    # check above
    if line > 0:
        for i in range(max(start-1, 0), min(end+1, maxLineIndex)+1):
            if isSymbol(inputList[line-1][i]):
                return True
    # check LR
    if start > 0:
        if isSymbol(inputList[line][start-1]):
            return True

    if end < maxLineIndex:
        if isSymbol(inputList[line][end+1]):
            return True

    # check below
    if line < len(inputList)-1:
        for i in range(max(start-1, 0), min(end+1, maxLineIndex)+1):
            if isSymbol(inputList[line+1][i]):
                return True

    return False


def main():
    curLine = 0
    start = None
    end = None
    sum = 0
    i = 0
    while curLine < len(inputList):
        if inputList[curLine][i].isnumeric() and start is None:
            start = i
        if inputList[curLine][i].isnumeric() and i < maxLineIndex:
            if not inputList[curLine][i+1].isnumeric():
                end = i
                if hasAdjacentSymbol(start, end, curLine):
                    sum += int(inputList[curLine][start:end+1])
                end = None
                start = None
        i += 1
        if i == maxLineIndex+1:
            end = i-1
            if start is not None:
                if hasAdjacentSymbol(start, end, curLine):
                    sum += int(inputList[curLine][start:end+1])

            start = None
            end = None
            i = 0
            curLine += 1

    print(sum)


if __name__ == "__main__":
    main()
