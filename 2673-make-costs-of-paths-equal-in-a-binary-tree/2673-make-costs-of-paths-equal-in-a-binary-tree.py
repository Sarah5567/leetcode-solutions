class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        max_from_leaf = [0] * (n + 1)
        res = 0
        for i in range(n, 0, -1):
            max_from_leaf[i] += cost[i - 1]
            max_from_leaf[i//2] = max(max_from_leaf[i//2], max_from_leaf[i])
            if i * 2 + 1 <= n:
                res += abs(max_from_leaf[i * 2] - max_from_leaf[i * 2 + 1])

        return res
        