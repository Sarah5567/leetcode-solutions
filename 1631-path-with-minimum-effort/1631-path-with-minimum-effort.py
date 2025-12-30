import heapq
from typing import List

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, cols = len(heights), len(heights[0])

        # dist[i][j] = minimum effort to reach (i, j)
        dist = [[float('inf')] * cols for _ in range(rows)]
        dist[0][0] = 0

        pq = [(0, 0, 0)]  # (current_effort, i, j)

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while pq:
            cur_dist, i, j = heapq.heappop(pq)

            if cur_dist > dist[i][j]:
                continue

            if i == rows - 1 and j == cols - 1:
                return cur_dist

            for di, dj in directions:
                ni, nj = i + di, j + dj
                if 0 <= ni < rows and 0 <= nj < cols:
                    effort = abs(heights[ni][nj] - heights[i][j])
                    new_dist = max(cur_dist, effort)

                    if new_dist < dist[ni][nj]:
                        dist[ni][nj] = new_dist
                        heapq.heappush(pq, (new_dist, ni, nj))

        return dist[rows - 1][cols - 1]
