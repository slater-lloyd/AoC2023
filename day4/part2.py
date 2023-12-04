def main():
    with open("day4/test.txt", "r") as f:
        i = 0
        lines = f.readlines()
        countOfCards = [1] * len(lines)
        for line in lines:
            line = line.split(":")
            scratched = line[1].split("|")

            winningNums = scratched[0].strip().split()
            cardNums = scratched[1].strip().split()

            winningCount = 0
            for num in cardNums:
                if num in winningNums:
                    winningCount += 1

            if winningCount >= 1:
                for y in range(1, winningCount+1):
                    countOfCards[i+y] += countOfCards[i]
            i += 1

        print(sum(countOfCards))


if __name__ == "__main__":
    main()
