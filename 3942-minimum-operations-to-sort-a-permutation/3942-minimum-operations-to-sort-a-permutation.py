class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        idx = nums.index(0)
        direction = 1 if nums[(idx - 1) % n] == n - 1 else -1

        for num in range(n):
            if nums[idx] != num:
                return -1
            idx = (idx + direction) % n

        if direction == 1:
            return min(idx, n - idx + 2)
        else:
            return min(idx + 2, n - idx)
