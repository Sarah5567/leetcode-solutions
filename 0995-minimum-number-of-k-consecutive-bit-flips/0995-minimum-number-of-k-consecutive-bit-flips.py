class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)

        flipped = 0
        ans = 0
        is_flipped = [0] * n

        for i in range(n):

            if i >= k:
                flipped ^= is_flipped[i - k]

            if nums[i] ^ flipped == 0:

                if i + k > n:
                    return -1

                ans += 1
                flipped ^= 1
                is_flipped[i] = 1

        return ans
