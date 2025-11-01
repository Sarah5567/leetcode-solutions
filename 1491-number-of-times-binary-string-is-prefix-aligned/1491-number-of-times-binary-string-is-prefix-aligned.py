class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        maxFlip, count = 0, 0

        for i in range(len(flips)):
            maxFlip = max(flips[i], maxFlip)
            if i == maxFlip - 1:
                count += 1

        return count