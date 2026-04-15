class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        max_base1 = int(c ** 0.5)

        for base1 in range(max_base1 + 1):
            base1_sq = base1 * base1
            base2_sq = c - base1_sq
            base2 = int(base2_sq ** 0.5)

            if base2 * base2 == base2_sq:
                return True

        return False
