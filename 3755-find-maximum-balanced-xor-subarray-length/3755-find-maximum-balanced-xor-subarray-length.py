class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        xors = {}
        diff = 0

        xors[(0,0)] = -1

        best = 0
        prefix_xor = 0
        for i, num in enumerate(nums):
            prefix_xor ^= num

            if num % 2:
                diff += 1
            else:
                diff -= 1

            if (prefix_xor, diff) in xors:
                best = max(best, i - xors[(prefix_xor, diff)])
            else:
                xors[(prefix_xor, diff)] = i

        return best
