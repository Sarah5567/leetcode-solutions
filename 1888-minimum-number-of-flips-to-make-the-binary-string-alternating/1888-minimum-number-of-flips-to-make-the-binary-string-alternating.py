class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        cost = 0
        
        for i, ch in enumerate(s):
            if (i % 2) != int(ch):
                cost += 1

        min_cost = min(cost, n - cost)

        for i, ch in enumerate(s):
            cost = n - 1 - cost
            digit = int(ch)

            if digit:
                cost += 1

            if ((n - 1) % 2) != digit:
                cost += 1

            min_cost = min(min_cost, cost, n - cost)
            if min_cost == 0:
                return 0

        return min_cost
