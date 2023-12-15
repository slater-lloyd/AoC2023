from sys import argv

input = []

inputFile = "day13/test.txt"

if len(argv) == 2:
    inputFile = argv[1]

with open(inputFile) as f:
    input = f.read().splitlines()


def parse(line):
    return line


def patternValue(pattern):
    for i in range(len(pattern)-1):
        if pattern[i] == pattern[i+1]:
            pairDist = 1
            while True:
                if i-pairDist < 0 or i+pairDist >= len(pattern)-1:
                    return (i+1)*100
                
                if pattern[i-pairDist] != pattern[i+pairDist+1]:
                    break
                
                pairDist += 1 

    for i in range(len(pattern[0])-1):
        if isPalindrome(pattern[0][i:]):
            allPals = True
            for line in pattern[1:]:
                if not isPalindrome(line[i:]):
                    allPals = False
            if allPals:
                return len(pattern[0])-(len(pattern[0])-i)/2

    pattern = [p[::-1] for p in pattern]
    for i in range(len(pattern[0])-1):
        if isPalindrome(pattern[0][i:]):
            allPals = True
            for line in pattern[1:]:
                if not isPalindrome(line[i:]):
                    allPals = False
            if allPals:
                return (len(pattern[0])-i)//2
    

def isPalindrome(s):
    return s == s[::-1]


def part1():
    counts = []
    curPattern = []
    for line in input:
        if line == "":
            counts.append(patternValue(curPattern))
            curPattern = []
        else:
            curPattern.append(line)
    counts.append(patternValue(curPattern))

    return sum(counts)

def hasOneError(p1, p2):
    errorCount = 0
    for i in range(len(p1)):
        if p1[i] != p2[i]:
            errorCount += 1 

    if errorCount == 1:
        return True
    return False


def isPalindromeV2(s):
    if s == s[::-1]:
        return True, 0
    errorCount = 0
    paired = [(s[x], s[0-x-1]) for x in range(int((len(s)//2)+0.5))]
    for pair in paired:
        if pair[0] != pair[1]:
            errorCount += 1 
            
    if errorCount > 1:
        return False, 0 
    return True, 1


def patternValueV2(pattern):
    for i in range(len(pattern)-1):
        errorCount = 0
        if pattern[i] == pattern[i+1] or hasOneError(pattern[i], pattern[i+1]):
            if hasOneError(pattern[i], pattern[i+1]):
                errorCount += 1 
            pairDist = 1
            while True:
                if (i-pairDist < 0 or i+pairDist >= len(pattern)-1) and errorCount == 1:
                    return (i+1)*100
                elif i-pairDist < 0 or i+pairDist >= len(pattern)-1:
                    break
                
                if pattern[i-pairDist] != pattern[i+pairDist+1] and errorCount == 0:
                    if hasOneError(pattern[i-pairDist], pattern[i+pairDist+1]):
                        errorCount += 1 
                    else:
                        break
                
                pairDist += 1 

    for i in range(len(pattern[0])-1):
        errorCount = 0
        isP, errorCount = isPalindromeV2(pattern[0][i:])
        if isP:
            allPals = True
            for line in pattern[1:]:
                isP, newError = isPalindromeV2(line[i:])
                errorCount += newError
                if not isP or errorCount > 1:
                    allPals = False
            if allPals and errorCount == 1:
                return len(pattern[0])-(len(pattern[0])-i)/2

    pattern = [p[::-1] for p in pattern]
    for i in range(len(pattern[0])-1):
        errorCount = 0
        isP, errorCount = isPalindromeV2(pattern[0][i:])
        if isP:
            allPals = True
            for line in pattern[1:]:
                isP, newError = isPalindromeV2(line[i:])
                errorCount += newError
                if not isP or errorCount > 1:
                    allPals = False
            if allPals and errorCount == 1:
                return (len(pattern[0])-i)//2
    
def part2():
    counts = []
    curPattern = []
    for line in input:
        if line == "":
            counts.append(patternValueV2(curPattern))
            curPattern = []
        else:
            curPattern.append(line)
    counts.append(patternValueV2(curPattern))

    print(counts)

    return sum(counts)


def main():
    print("Part 1:", part1())
    print("Part 2:", part2())


if __name__ == "__main__":
    main()
