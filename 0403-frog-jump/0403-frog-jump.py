class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_to_index = {stone: i for i, stone in enumerate(stones)}
        n = len(stones)

        dp = [set() for _ in range(n)]
        dp[0].add(0)

        for i in range(n):
            for k in dp[i]:
                for jump in (k - 1, k, k + 1):
                    if jump <= 0:
                        continue

                    next_pos = stones[i] + jump
                    if next_pos in stone_to_index:
                        dp[stone_to_index[next_pos]].add(jump)

        return bool(dp[-1])
