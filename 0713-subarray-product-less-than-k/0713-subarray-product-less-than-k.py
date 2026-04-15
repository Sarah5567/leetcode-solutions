class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0

        product = nums[0]
        count = 0
        l, r = 0, 0

        while r < len(nums):
            if product >= k:
                product /= nums[l]
                l += 1
            else:
                count += r - l + 1
                r += 1
                if r < len(nums):
                    product *= nums[r]

        return count
