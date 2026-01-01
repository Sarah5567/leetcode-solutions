class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        max_from_leaf = [0] * (n + 1)
        for i in range(n, 0, -1):
            cur = max_from_leaf[i] + cost[i - 1]
            parent = i // 2
            max_from_leaf[i] = cur
            if parent > 0:
                max_from_leaf[parent] = max(max_from_leaf[parent], cur)

        target = max_from_leaf[1]

        max_from_root = [0] * (n + 1)

        def min_increment(i: int) -> int:
            if i > n:
                return 0

            parent = i // 2
            left = i * 2
            right = left + 1

            max_from_root[i] = max_from_root[parent] + cost[i - 1]
            inc = target - max_from_root[parent] - max_from_leaf[i]
            max_from_root[i] += inc

            return inc + min_increment(left) + min_increment(right)

        return min_increment(1)
