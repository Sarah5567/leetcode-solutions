class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        length1, length2 = 1, 1

        for i in range(1, len(nums)):
            if (nums[i] > nums[i - 1] and length1 % 2) or (nums[i] < nums[i - 1] and not length1 % 2):
                length1 += 1
            if (nums[i] < nums[i - 1] and length2 % 2) or (nums[i] > nums[i - 1] and not length2 % 2):
                length2 += 1

        return max(length1, length2)
