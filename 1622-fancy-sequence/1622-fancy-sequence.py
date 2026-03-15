class Fancy:
    MOD = 1000000007

    def __init__(self):
        self.global_mul = 1
        self.global_add = 0
        self.base_values = []

    def append(self, val: int) -> None:
        inv = pow(self.global_mul, self.MOD - 2, self.MOD)
        new_val = (val - self.global_add) * inv % self.MOD
        self.base_values.append(new_val)

    def addAll(self, inc: int) -> None:
        self.global_add = (self.global_add + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.global_mul = (self.global_mul * m) % self.MOD
        self.global_add = (self.global_add * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx >= len(self.base_values):
            return -1
        return (self.base_values[idx] * self.global_mul + self.global_add) % self.MOD