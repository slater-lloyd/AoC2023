class BlockNode:
    def __init__(self, weight) -> None:
        self.weight = int(weight)
        self.up = None
        self.down = None
        self.left = None
        self.right= None
