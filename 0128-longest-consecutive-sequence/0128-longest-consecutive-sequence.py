class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            if num - 1 not in nums_set:
                current = num
                length = 1
                while current + 1 in nums_set:
                    current += 1
                    length += 1
                longest = max(longest, length)
        
        return longest
