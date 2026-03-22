class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda p: p[1])

        arrows = 0
        arrow_pos = float('-inf')
        for start, end in points:
            if arrow_pos < start:
                arrows += 1
                arrow_pos = end

        return arrows
