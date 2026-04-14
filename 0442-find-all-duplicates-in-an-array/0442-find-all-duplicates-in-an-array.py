class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []

        for x in nums:
            idx = abs(x) - 1
            val = nums[idx]

            if val < 0:
                duplicates.append(idx + 1)
            else:
                nums[idx] = -val

        return duplicates