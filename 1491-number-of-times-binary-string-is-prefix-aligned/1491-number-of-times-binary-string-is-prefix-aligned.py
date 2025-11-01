class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        maxFlip, count = 0, 0

        for i, flip in enumerate(flips):
            maxFlip = max(flip, maxFlip)
            if i == maxFlip - 1:
                count += 1

        return count