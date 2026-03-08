class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)

        flipped = 0          # parity of active flips
        ans = 0              # number of flips
        is_flipped = [0] * n # marks where a flip started

        for i in range(n):

            # remove flip effect when leaving the window
            if i >= k:
                flipped ^= is_flipped[i - k]

            # check current bit after flips
            if nums[i] ^ flipped == 0:

                if i + k > n:
                    return -1

                ans += 1
                flipped ^= 1
                is_flipped[i] = 1

        return ans
