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

def main():
    print("Part 1:", part1())


if __name__ == "__main__":
    main()
