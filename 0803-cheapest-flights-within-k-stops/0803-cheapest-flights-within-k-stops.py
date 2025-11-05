from collections import defaultdict, deque
from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))

        # stops[i][v] = min cost to reach v with i stops
        stops = [[float('inf')] * n for _ in range(k + 2)]
        stops[0][src] = 0

        # single queue to avoid storing redundant data
        q = deque([(src, 0, 0)])  # (current node, cost, stops_used)

        while q:
            u, cost, stop = q.popleft()
            if stop > k or cost > stops[stop][u]:
                continue
            for v, w in graph[u]:
                new_cost = cost + w
                # update only if we found cheaper path
                if new_cost < stops[stop + 1][v]:
                    stops[stop + 1][v] = new_cost
                    q.append((v, new_cost, stop + 1))

        cheapest = min(stops[i][dst] for i in range(k + 2))
        return cheapest if cheapest < float('inf') else -1