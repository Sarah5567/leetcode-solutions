class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        
        return sum(nums[i] for i in range(int(n / 3), n, 2))