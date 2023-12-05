class AlmanacLine:
    def __init__(self, dest, source, rng):
        self.dest = dest
        self.source = source
        self.rng = rng

    def isInRange(self, num):
        if num >= self.source and num <= self.source+self.rng:
            return True
        return False

    def isInDestRange(self, num):
        if num >= self.dest and num <= self.dest+self.rng:
            return True
        return False

    def getConverted(self, num):
        if self.isInRange(num):
            return num - self.source + self.dest
        print(f"Tried to convert out of range number: {num}")
        return False

    def unConvert(self, num):
        return num - self.dest + self.source

    def __str__(self):
        return f"{self.dest} {self.source} {self.rng}"
