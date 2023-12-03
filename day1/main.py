textNums = {
    "one": "on1ne",
    "two": "tw2wo",
    "three": "th3ee",
    "four": "fo4ur",
    "five": "fi5ve",
    "six": "si6ix",
    "seven": "sev7ven",
    "eight": "eig8ght",
    "nine": "ni9ne",
    "zero": "ze0ro"
}


def replaceTextWithNums(strVal):
    for key in textNums.keys():
        strVal = strVal.replace(key, str(textNums[key]))
    return strVal


def findNum(line, forward=True):
    if not forward:
        line = reversed(line)

    for i in line:
        if i.isnumeric():
            return int(i)


def main():
    sum = 0

    with open("test.txt", "r") as testFile:
        for line in testFile.readlines():
            line = replaceTextWithNums(line.strip())
            tens = findNum(line, True) * 10
            ones = findNum(line, False)
            print(tens+ones)
            sum += tens+ones

    print(f"sum: {sum}")


if __name__ == "__main__":
    main()
