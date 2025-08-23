from typing import List
from collections import defaultdict

class Solution:
    def line_base_slope(self, p1, p2):
        x1, y1 = p1
        x2, y2 = p2

        if x1 == x2:
            return (float('inf'), x1)  # vertical line

        slope = (y2 - y1) / (x2 - x1)
        slope = round(slope, 10)  # avoid float precision errors
        intercept = y1 - slope * x1
        intercept = round(intercept, 10)
        return (slope, intercept)

    def maxPoints(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        n = len(points)
        if n <= 2:
            return n

        longestLine = 0

        for i in range(n):
            lines = defaultdict(int)
            duplicates = 1
            for j in range(i+1, n):
                if points[i] == points[j]:
                    duplicates += 1
                else:
                    line = self.line_base_slope(points[i], points[j])
                    lines[line] += 1

            max_line = max(lines.values(), default=0)
            longestLine = max(longestLine, max_line + duplicates)

        return longestLine
