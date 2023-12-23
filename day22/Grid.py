class Grid:
    def __init__(self, arr) -> None:
        self.arr = arr

    def printFace(self, ind=0, rotate=False):
        if not rotate:
            for heightI, height in reversed(list(enumerate(self.arr))):
                for colI, col in enumerate(height):
                    print(self.arr[heightI][colI][ind], end=" ")
                print(f"({heightI})")
        else:
            for heightI, height in reversed(list(enumerate(self.arr))):
                for rowI, row in enumerate(height[ind]):
                    print(self.arr[heightI][ind][rowI], end=" ")
                print(f"({heightI})")
