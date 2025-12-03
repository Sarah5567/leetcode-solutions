class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        m = len(nums)
        n = len(nums[0])
        score = 0

        nums = [sorted(row, reverse=True) for row in nums]

        for j in range(n):
            maxValue = 0
            for i in range(m):
                maxValue = max(maxValue, nums[i][j])
            score += maxValue

        return score
        