class Solution:
    def rob(self, nums: List[int]) -> int:
        h1, h2, h3 = 0, 0, 0

        for num in nums:
            h1, h2, h3 = h2, h3, max(h1, h2) + num

        return max(h1, h2, h3)
        