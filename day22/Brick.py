class Brick:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
        self.length = max([abs(start[i]-end[i]) for i in range(len(start))])
        self.dir = max([i if abs(start[i]-end[i]) > 0 else -1 for i in range(len(start))])

    def getAllCoords(self):
        blocks = []
        curBlock = self.start.copy()
        for _ in range(self.length):
            curBlock[self.dir] += 1
            blocks.append(Block(curBlock[0], curBlock[1], curBlock[2]))
        return blocks

    def __str__(self) -> str:
        return f"{self.start}~{self.end} ({self.length})"

class Block:
    def __init__(self, row, col, hei) -> None:
        self.row = row
        self.col = col
        self.hei = hei
