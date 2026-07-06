class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        rightmost = -1
        remainings = 0

        for l, r in intervals:
            if r > rightmost:
                rightmost = r
                remainings += 1

        return remainings
