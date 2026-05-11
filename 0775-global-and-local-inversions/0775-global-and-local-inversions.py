class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        mx = nums[0]
        n = len(nums)

        for i in range(n - 2):
            if nums[i] > mx:
                mx = nums[i]

            if mx > nums[i + 2]:
                return False

        return True