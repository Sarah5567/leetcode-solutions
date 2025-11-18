class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        curBorder, nextBorder = 1, 1
        for i, num in enumerate(nums):
            if i == curBorder:
                jumps += 1
                curBorder = nextBorder
            nextBorder = max(nextBorder, i + num + 1)

        return jumps
