def main():
    sum = 0
    with open("day4/test.txt", "r") as f:
        for line in f.readlines():
            line = line.split(":")
            scratched = line[1].split("|")

            winningNums = scratched[0].strip().split()
            cardNums = scratched[1].strip().split()

            winningCount = 0.5
            for num in cardNums:
                if num in winningNums:
                    winningCount *= 2

            if winningCount >= 1:
                sum += winningCount

    print(sum)


if __name__ == "__main__":
    main()
