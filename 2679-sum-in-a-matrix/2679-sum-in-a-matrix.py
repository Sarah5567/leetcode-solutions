class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        nums = [sorted(row, reverse=True) for row in nums]

        return sum(max(col) for col in zip(*nums))
