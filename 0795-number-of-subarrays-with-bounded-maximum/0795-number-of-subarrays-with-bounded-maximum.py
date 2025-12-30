class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        too_large_prev = -1
        too_small_length = 0
        ans = 0

        def count(length: int) -> int:
            return length * (length + 1) // 2

        for i, num in enumerate(nums):
            if num >= left:
                if too_small_length:
                    ans -= count(too_small_length)
                    too_small_length = 0

                if num > right:
                    ans += count(i - too_large_prev - 1)
                    too_large_prev = i
            else:
                too_small_length += 1

        ans += count(len(nums) - 1 - too_large_prev)

        if too_small_length:
            ans -= count(too_small_length)

        return ans
