class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        longest = 0
        seen = set()

        for l in range(n):
            balance = 0

            for r in range(l, n):
                if nums[r] not in seen:
                    seen.add(nums[r])
                    balance += (1 if nums[r] % 2 else -1)
                if balance == 0:
                    longest = max(longest, r - l + 1)
            seen.clear()
            
        return longest
                      