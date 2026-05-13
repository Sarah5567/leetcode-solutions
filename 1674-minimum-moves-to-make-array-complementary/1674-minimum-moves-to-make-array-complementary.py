class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        diffs = [0] * (limit * 2 + 2)

        for i in range(n // 2):
            x = nums[i]
            y = nums[n - i - 1]

            diffs[0] += 2
            diffs[min(x, y) + 1] -= 1
            diffs[x + y] -= 1
            diffs[x + y + 1] += 1
            diffs[max(x, y) + limit + 1] += 1

        min_moves = diffs[0]
        total = 0
        for diff in diffs:
            total += diff
            min_moves = min(min_moves, total)

        return min_moves


