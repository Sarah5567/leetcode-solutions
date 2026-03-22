class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda point: point[0])
        arrows = 0
        arrow_pos = float('-inf')
        for start, end in points:
            if arrow_pos >= start:
                arrow_pos = min(arrow_pos, end)
            else:
                arrows += 1
                arrow_pos = end

        return arrows
