class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        flips = [0] * len(nums)
        
        for i, num in enumerate(nums):

            if i > 0:
                flips[i] = flips[i - 1]

            last_k_flips = flips[i - 1] if i > 0 else 0
            if i >= k:
                last_k_flips -= flips[i - k]

            if (num + last_k_flips) % 2 == 0:
                if i + k > len(nums):
                    return -1
                flips[i] += 1

        return flips[-1]
