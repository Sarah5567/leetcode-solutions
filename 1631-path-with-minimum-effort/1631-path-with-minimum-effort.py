class Solution:
    def dijkstra(self, graph, start):
        dist = {node : float('inf') for node in graph}
        dist[start] = 0

        pq = [(0, start)]
        while pq:
            cur_dist, u = heapq.heappop(pq)
            if cur_dist > dist[u]:
                continue

            for v, w in graph[u]:
                new_dist = max(cur_dist, w)
                if new_dist < dist[v]:
                    dist[v] = new_dist
                    heapq.heappush(pq, (new_dist, v))

        return dist

    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows, columns = len(heights), len(heights[0])
        graph = {(i, j) : [] for i in range(rows) for j in range(columns)}
        for i in range(rows):
            for j in range(columns):
                if i > 0:
                    effort = abs(heights[i - 1][j] - heights[i][j])
                    graph[(i, j)].append(((i - 1, j), effort))
                    graph[(i - 1, j)].append(((i, j), effort))
                 
                if j > 0:
                    effort = abs(heights[i][j - 1] - heights[i][j])
                    graph[(i, j)].append(((i, j - 1), effort))
                    graph[(i, j - 1)].append(((i, j), effort))

        dist = self.dijkstra(graph, (0, 0))
        return int(dist[(rows-1, columns-1)])
