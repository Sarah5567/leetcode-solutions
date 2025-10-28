class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxIdx, curIdx = 0, 0
        while curIdx <= min(maxIdx, len(nums) - 1):
            maxIdx = max(maxIdx, curIdx + nums[curIdx])
            curIdx += 1
        
        return curIdx == len(nums)