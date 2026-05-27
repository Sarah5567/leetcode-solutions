class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        is_sorted = True
        bitwise_and = 0

        for i, num in enumerate(nums):
            if i != num:
                bitwise_and = bitwise_and & num if not is_sorted else num
                is_sorted = False

        return bitwise_and
