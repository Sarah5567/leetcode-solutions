class Bitset:

    def __init__(self, size: int):
        self.bits = [False] * size
        self.count_ones = 0
        self.is_fliped = False

    def fix(self, idx: int) -> None:
        if self.bits[idx] == self.is_fliped:
            self.bits[idx] = not self.bits[idx]
            self.count_ones += 1

    def unfix(self, idx: int) -> None:
        if self.bits[idx] != self.is_fliped:
            self.bits[idx] = not self.bits[idx]
            self.count_ones -= 1

    def flip(self) -> None:
        self.is_fliped = not self.is_fliped
        self.count_ones = len(self.bits) - self.count_ones

    def all(self) -> bool:
        return self.count_ones == len(self.bits)

    def one(self) -> bool:
        return self.count_ones > 0

    def count(self) -> int:
        return self.count_ones

    def toString(self) -> str:
        return ''.join('1' if bit != self.is_fliped else '0' for bit in self.bits)

# Your Bitset object will be instantiated and called as such:
# obj = Bitset(size)
# obj.fix(idx)
# obj.unfix(idx)
# obj.flip()
# param_4 = obj.all()
# param_5 = obj.one()
# param_6 = obj.count()
# param_7 = obj.toString()