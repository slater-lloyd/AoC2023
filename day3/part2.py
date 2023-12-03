inputList = []
with open("test.txt", "r") as f:
    for line in f.readlines():
        inputList.append(line.strip())
maxLineIndex = len(inputList[0])-1
chars = ["=", "@", "#", "$", "%", "-", "&", "*", "/", "+"]


def getFullNum(pos, line):
    start = pos
    end = pos
    while start > 0:
        if inputList[line][start-1].isnumeric():
            start -= 1
        else:
            break

    while end < maxLineIndex:
        if inputList[line][end+1].isnumeric():
            end += 1
        else:
            break

    return inputList[line][start:end+1]


def getAdjacentNums(pos, line):
    nums = []
    # check above
    if line > 0:
        if inputList[line-1][pos].isnumeric():
            nums.append(int(getFullNum(pos, line-1)))
        else:
            if pos > 0:
                if inputList[line-1][pos-1].isnumeric():
                    nums.append(int(getFullNum(pos-1, line-1)))
            if pos < maxLineIndex:
                if inputList[line-1][pos+1].isnumeric():
                    nums.append(int(getFullNum(pos+1, line-1)))

    # check LR
    if pos > 0:
        if inputList[line][pos-1].isnumeric():
            nums.append(int(getFullNum(pos-1, line)))
    if pos < maxLineIndex:
        if inputList[line][pos+1].isnumeric():
            nums.append(int(getFullNum(pos+1, line)))

    # check below
    if line < len(inputList)-1:
        if inputList[line+1][pos].isnumeric():
            nums.append(int(getFullNum(pos, line+1)))
        else:
            if pos > 0:
                if inputList[line+1][pos-1].isnumeric():
                    nums.append(int(getFullNum(pos-1, line+1)))
            if pos < maxLineIndex:
                if inputList[line+1][pos+1].isnumeric():
                    nums.append(int(getFullNum(pos+1, line+1)))

    return nums


def main():
    sum = 0
    for line in range(len(inputList)):
        for i in range(len(inputList[0])):
            if inputList[line][i] == "*":
                nums = getAdjacentNums(i, line)
                if len(nums) == 2:
                    sum += nums[0] * nums[1]
    print(sum)


if __name__ == "__main__":
    main()
