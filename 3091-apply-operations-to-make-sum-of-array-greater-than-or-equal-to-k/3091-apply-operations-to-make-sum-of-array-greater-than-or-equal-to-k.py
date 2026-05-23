class Solution:
    def minOperations(self, k: int) -> int:
        best = k - 1

        for i in range(1, math.ceil(k ** 0.5) + 1):
            best = min(best, i + math.ceil(k / i) - 2)

        return best
