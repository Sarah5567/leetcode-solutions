class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []

        for i in range(len(nums)):
            while True:
                target = nums[i] - 1

                if i == target or nums[i] == nums[target]:
                    break

                nums[i], nums[target] = nums[target], nums[i]

        for i in range(len(nums)):
            if nums[i] != i + 1:
                duplicates.append(nums[i])

        return duplicates
