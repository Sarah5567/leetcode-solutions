class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        def min_increment(i) -> int:
            if i > n:
                return 0

            max_from_root[i] = max_from_root[i // 2] + cost[i - 1]
            increament = max_from_leaf[1] - max_from_root[i // 2] - max_from_leaf[i]
            max_from_root[i] += increament
            return increament + min_increment(i * 2) + min_increment(i * 2 + 1) 

        max_from_leaf = [0] * (n + 1)
        for i in range(n, 0, -1):
            max_from_leaf[i] += cost[i - 1]
            max_from_leaf[i//2] = max(max_from_leaf[i//2], max_from_leaf[i])

        max_from_root = [0] * (n + 1)
        return min_increment(1)