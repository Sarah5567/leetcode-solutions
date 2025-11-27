class Solution:
    def splitArraySameAverage(self, nums):
        n = len(nums)
        total = sum(nums)

        # Early pruning: if no subset size k satisfies integer sum condition
        possible = False
        for k in range(1, n):
            if (total * k) % n == 0:
                possible = True
                break
        if not possible:
            return False

        nums.sort()

        @lru_cache(None)
        def dfs(i, k, target):
            if k == 0:
                return target == 0
            if i == n or k < 0 or target < 0:
                return False

            # choose nums[i]
            if dfs(i + 1, k - 1, target - nums[i]):
                return True

            # skip nums[i]
            return dfs(i + 1, k, target)

        for k in range(1, n):
            # only check subset sizes where target sum is integer
            if (total * k) % n == 0:
                target = (total * k) // n
                if dfs(0, k, target):
                    return True

        return False

