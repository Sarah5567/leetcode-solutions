from functools import lru_cache
from bisect import bisect_left, bisect_right

class Solution:
    def splitArraySameAverage(self, nums):
        n = len(nums)
        total = sum(nums)

        # Early pruning
        for k in range(1, n):
            if (total * k) % n == 0:
                break
        else:
            return False

        nums.sort()
        loc_nums = nums
        loc_n = n

        @lru_cache(None)
        def dfs(i, k, target):
            # Same logic, just faster lookups
            if k == 0:
                return target == 0
            if i == loc_n or target < 0 or k < 0:
                return False

            # choose
            if dfs(i + 1, k - 1, target - loc_nums[i]):
                return True

            # skip
            return dfs(i + 1, k, target)

        for k in range(1, n):
            if (total * k) % n != 0:
                continue

            target = (total * k) // n

            # small pruning (sum range possible using sorted nums)
            # does NOT change logic – just avoids impossible calls
            if target < loc_nums[0] * min(k, loc_n) or target > loc_nums[-1] * k:
                continue

            if dfs(0, k, target):
                return True

        return False
