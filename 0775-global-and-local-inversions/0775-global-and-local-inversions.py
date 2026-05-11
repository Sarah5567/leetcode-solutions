class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        max_value = float('-inf')

        for i in range(len(nums) - 2):
            max_value = max(max_value, nums[i])
            if max_value > nums[i + 2]:
                return False

        return True