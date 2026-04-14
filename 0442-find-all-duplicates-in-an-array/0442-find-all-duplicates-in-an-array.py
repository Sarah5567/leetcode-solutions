class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        n = len(nums)

        for i in range(n):
            while nums[i] != nums[nums[i] - 1]:
                target = nums[i] - 1
                nums[i], nums[target] = nums[target], nums[i]

        for i in range(n):
            if nums[i] != i + 1:
                duplicates.append(nums[i])

        return duplicates
