class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        curBorder, nextBorder = 1, 1
        for i in range(len(nums)):
            if i == curBorder:
                jumps += 1
                curBorder = nextBorder
            nextBorder = max(nextBorder, i + nums[i] + 1)

        return jumps
