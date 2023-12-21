from re import findall


class Gear:
    def __init__(self, x, m, a, s):
        self.x = x 
        self.m = m 
        self.a = a
        self.s = s

    def sumParts(self):
        return self.x + self.m + self.a + self.s

    def __str__(self) -> str:
        return f"X:{self.x}, M:{self.m}, A:{self.a}, S:{self.s}"

class Rule:
    def __init__(self, criteria, dist) -> None:
        self.dist = dist
        self.isGT = False
        self.gearKey = None
        self.criteria = None
        if criteria:
            if ">" in criteria:
                self.isGT = True

            self.criteria = int(findall(r'\d+', criteria)[0])
            self.gearKey = criteria[0]

    def meetsRule(self, gear):
        if self.criteria is None:
            return True
        
        val = gear.s
        if self.gearKey == "x":
            val = gear.x
        elif self.gearKey == "m":
            val = gear.m 
        elif self.gearKey == "a":
            val = gear.a 

        if self.isGT:
            return val > self.criteria
        return val < self.criteria

    def __str__(self):
        sym = "<"
        if self.isGT:
            sym = ">"
        return f"{self.gearKey} {sym} {self.criteria} -> {self.dist}"

class WorkFlow:
    def __init__(self, rules) -> None:
        self.rules = rules

    def process(self, gear: Gear) -> str:
        for rule in self.rules:
            if rule.meetsRule(gear):
                return rule.dist
        print(f"Error processing gear: {gear}")
        return "Did not work"
