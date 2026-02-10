class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        longest = 0

        for l in range(n):
            distinct_nums = set()
            balance = 0

            for r in range(l, n):
                if nums[r] not in distinct_nums:
                    distinct_nums.add(nums[r])
                    balance += (1 if nums[r] % 2 else -1)
                if balance == 0:
                    longest = max(longest, r - l + 1)
            
        return longest
                      