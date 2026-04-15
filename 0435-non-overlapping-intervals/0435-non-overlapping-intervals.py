class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])

        cur_edge = float('-inf')
        removed = 0

        for start, end in intervals:
            if start >= cur_edge:
                cur_edge = end
            else:
                removed += 1

        return removed
