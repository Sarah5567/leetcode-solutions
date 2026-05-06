class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []

        index = 0
        while index < len(intervals) and intervals[index][1] < newInterval[0]:
            ans.append(intervals[index])
            index += 1

        if index == len(intervals):
            return ans + [newInterval]

        start = min(intervals[index][0], newInterval[0])
        end = newInterval[1]

        while index < len(intervals) and intervals[index][0] <= newInterval[1]:
            end = max(end, intervals[index][1])
            index += 1

        ans.append([start, end])

        while index < len(intervals):
            ans.append(intervals[index])
            index += 1

        return ans
        