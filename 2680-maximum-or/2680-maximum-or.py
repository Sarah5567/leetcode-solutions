class Solution:
    def maximumOr(self, nums: List[int], k: int) -> int:
        n = len(nums)
        others_or = [0] * n
        prefix = 0
        suffix = 0

        for i in range(n):
            others_or[i] |= prefix
            others_or[n - i - 1] |= suffix

            prefix |= nums[i]
            suffix |= nums[n - i - 1]

        best = 0
        for num, or_operation in zip(nums, others_or):
            best = max(best, or_operation | num << k)
        
        return best
