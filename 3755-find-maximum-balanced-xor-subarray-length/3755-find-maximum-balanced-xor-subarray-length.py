class Solution:
    def maxBalancedSubarray(self, nums: List[int]) -> int:
        seen_states = {}
        seen_states[(0,0)] = -1
        
        diff = 0
        best = 0
        prefix_xor = 0
        for i, num in enumerate(nums):
            prefix_xor ^= num

            if num % 2:
                diff += 1
            else:
                diff -= 1

            if (prefix_xor, diff) in seen_states:
                best = max(best, i - seen_states[(prefix_xor, diff)])
            else:
                seen_states[(prefix_xor, diff)] = i

        return best
