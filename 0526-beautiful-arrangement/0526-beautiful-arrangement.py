class Solution:
    def backtrack(self, placed, i):
        if i == len(placed):
            return 1

        ways = 0
        for j in range(1, len(placed)):
            if not placed[j] and (j % i == 0 or i % j == 0):
                placed[j] = True
                ways += self.backtrack(placed, i + 1)
                placed[j] = False

        return ways
        
    def countArrangement(self, n: int) -> int:
        placed = [False] * (n + 1)
        return self.backtrack(placed, 1)
