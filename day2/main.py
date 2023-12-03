class Game:
    def __init__(self, id, redMax, greenMax, blueMax):
        self.id = id
        self.redMax = redMax
        self.greenMax = greenMax
        self.blueMax = blueMax

    def isValid(self, redVal, greenVal, blueVal):
        if self.redMax <= redVal and self.greenMax <= greenVal and self.blueMax <= blueVal:
            return True
        return False

    def getGamePower(self):
        return self.redMax * self.greenMax * self.blueMax

    def __str__(self):
        return f"{self.id}: red: {self.redMax}, green: {self.greenMax}, blue: {self.blueMax}"


def getVal(pull):
    pullAsList = pull.split()
    intVal = int(pullAsList[0])
    return intVal


def createGame(line):
    line = line.strip().replace("Game ", "").replace(";", ":").replace(",", ":")
    line = line.split(":")
    redMax = 0
    greenMax = 0
    blueMax = 0
    for pull in line[1:]:
        pull = pull.strip()
        if "red" in pull:
            redMax = max(redMax, getVal(pull))
        elif "green" in pull:
            greenMax = max(greenMax, getVal(pull))
        else:
            blueMax = max(blueMax, getVal(pull))
    return Game(int(line[0]), redMax, greenMax, blueMax)


def main():
    sum = 0

    games = []
    with open("test.txt", "r") as testFile:
        for line in testFile.readlines():
            games.append(createGame(line))

    for game in games:
        sum += game.getGamePower()
    print(sum)


if __name__ == "__main__":
    main()
