class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        base1 = 1
        max_base1 = int((c // 2) ** 0.5)

        for base1 in range(max_base1 + 1):
            base2 = (c - base1 ** 2) ** 0.5
            if base2 == int(base2):
                return True

        return False
