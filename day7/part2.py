from functools import cmp_to_key

input = []

with open("day7/test2.txt", "r") as f:
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
    cards = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]
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
    for card in hand:
        if hand.count(card) == 5 or (hand.count(card)+hand.count("J") == 5 and card != "J"):
            print(f"Five of kind: {hand}")
            return True
    return False


def isFourOfKind(hand):
    for card in hand:
        if hand.count(card) == 4 or (hand.count(card)+hand.count("J") == 4 and card != "J"):
            print(f"Four of kind: {hand}")
            return True
    return False


def isFullHouse(hand):
    test = hand
    handSet = set(hand)
    has2 = False
    has3 = False
    for card in handSet:
        if hand.count(card) == 3:
            hand = hand.replace(card, "")
            has3 = True
        elif hand.count(card) == 2 and "J" in hand:
            hand = hand.replace(card, "")
            hand = hand.replace('J', '')
            has3 = True
        elif hand.count(card) == 2:
            hand = hand.replace(card, "")
            has2 = True

    if has2 and has3:
        print(f"Full house: {test}")
        return True
    return False


def isThreeOfKind(hand):
    for card in hand:
        if hand.count(card) == 3 or (hand.count(card)+hand.count("J") == 3 and card != "J"):
            print(f"Three of kind: {hand}")
            return True
    return False


def isTwoPair(hand):
    pairCount = 0
    test = hand
    handSet = set(hand)
    for card in handSet:
        if hand.count(card) == 1 and "J" in hand:
            hand = hand.replace(card, "")
            hand = hand.replace('J', '')
            pairCount += 1
        elif hand.count(card) == 2:
            hand = hand.replace(card, "")
            pairCount += 1

    if pairCount == 2:
        print(f"Two pair: {test}")
        return True
    return False


def isPair(hand):
    handSet = set(hand)
    if len(handSet) == 5 and "J" in handSet:
        print(f"Pair: {hand}")
        return True
    elif len(handSet) == 4:
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
