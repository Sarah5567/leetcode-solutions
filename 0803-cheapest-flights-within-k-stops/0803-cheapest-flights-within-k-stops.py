class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        stops = [[float('inf')] * n for _ in range(k + 2)]
        stops[0][src] = 0

        q = deque()
        for v, w in graph[src]:
            q.append((src, v, w, 1))

        for stop in range(1, k + 2):
            while q and q[0][-1] == stop:
                u, v, w, stop = q.popleft()
                if stops[stop][v] == float('inf'):
                    for neighbor, weight in graph[v]:
                        q.append((v, neighbor, weight, stop + 1))
                stops[stop][v] = min(stops[stop][v], stops[stop - 1][u] + w)

        cheapest = min(stops[i][dst] for i in range(k + 2))
        return cheapest if cheapest < float('inf') else -1