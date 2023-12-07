from functools import cmp_to_key

input = []

with open("day7/test.txt", "r") as f:
    input = f.read().splitlines()


def parse(line):
    return line.split()


def compare(x, y):
    xVal = getVal(x)
    yVal = getVal(y)
    if xVal > yVal:
        return 1
    elif yVal > xVal:
        return -1
    else:
        for i in range(5):
            xInt = cardToInt(x[i])
            yInt = cardToInt(y[i])
            if xInt > yInt:
                return 1
            elif yInt > xInt:
                return -1
    return 0


def cardToInt(card):
    cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    return 13-cards.index(card)


def getVal(hand):
    if isFiveOfKind(hand):
        return 6
    elif isFourOfKind(hand):
        return 5
    elif isFullHouse(hand):
        return 4
    elif isThreeOfKind(hand):
        return 3
    elif isTwoPair(hand):
        return 2
    elif isPair(hand):
        return 1
    return 0


def isFiveOfKind(hand):
    if hand.count(hand[0]) == 5:
        print(f"Five of kind: {hand}")
        return True
    return False


def isFourOfKind(hand):
    for card in hand:
        if hand.count(card) == 4:
            print(f"Four of kind: {hand}")
            return True
    return False


def isFullHouse(hand):
    has2 = False
    has3 = False
    for card in hand:
        if hand.count(card) == 2:
            has2 = True
        elif hand.count(card) == 3:
            has3 = True

    if has2 and has3:
        print(f"Full house: {hand}")
        return True
    return False


def isThreeOfKind(hand):
    for card in hand:
        if hand.count(card) == 3:
            print(f"Three of kind: {hand}")
            return True
    return False


def isTwoPair(hand):
    pairCount = 0
    for card in hand:
        if hand.count(card) == 2:
            pairCount += 1

    if pairCount == 4:
        print(f"Two pair: {hand}")
        return True
    return False


def isPair(hand):
    for card in hand:
        if hand.count(card) == 2:
            print(f"Pair: {hand}")
            return True
    return False


def main():
    hands = [parse(line) for line in input]
    hands = sorted(hands, key=cmp_to_key(
        lambda x, y: compare(x[0], y[0])))

    sum = 0
    for i, hand in enumerate(hands):
        sum += int(hand[1])*(i+1)
        print(hand[1], i+1)

    print(sum)


if __name__ == "__main__":
    main()
