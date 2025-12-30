class Solution:
    def get_num_subarrays(self, length: int) -> int:
        return length * (length + 1) // 2

    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        too_large_prev = -1
        too_small_length = 0
        ans : long = 0
        for i, num in enumerate(nums):
            if left <= num:
                ans -= self.get_num_subarrays(too_small_length)
                too_small_length = 0
                if right < num:
                    ans += self.get_num_subarrays(i - too_large_prev - 1)
                    too_large_prev = i
            else:
                too_small_length += 1

        ans += self.get_num_subarrays(len(nums) - 1 - too_large_prev)
        ans -= self.get_num_subarrays(too_small_length)

        return int(ans)