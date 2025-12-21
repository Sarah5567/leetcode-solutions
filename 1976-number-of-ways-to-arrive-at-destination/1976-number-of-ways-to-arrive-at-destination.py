class Solution:
    def dijkstra(
        self,
        n: int,
        graph: List[List[Tuple[int, int]]],
        source: int
    ) -> List[List[int]]:

        INF = 10**18
        dist: List[int] = [INF] * n
        dist[source] = 0

        shortest_ways: List[List[int]] = [[] for _ in range(n)]

        priority_queue: List[Tuple[int, int]] = []
        heapq.heappush(priority_queue, (0, source))

        while priority_queue:
            current_dist, u = heapq.heappop(priority_queue)

            # Skip outdated entries
            if current_dist > dist[u]:
                continue

            for v, weight in graph[u]:
                new_dist = current_dist + weight

                if new_dist == dist[v]:
                    shortest_ways[v].append(u)
                elif new_dist < dist[v]:
                    dist[v] = new_dist
                    shortest_ways[v] = [u]
                    heapq.heappush(priority_queue, (new_dist, v))

        return shortest_ways

    def dfs(self, shortest_ways: List[List[int]], counts : List[int], u : int, MOD: int) -> None:
        if counts[u] != -1:
            return

        counts[u] = 0
        for shortest_v in shortest_ways[u]:
            self.dfs(shortest_ways, counts, shortest_v, MOD)
            counts[u] = (counts[u] + counts[shortest_v]) % MOD


    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7

        graph : List[List[Tuple[int, int]]] = [[] for _ in range(n)]
        for road in roads:
            u, v, t = road
            graph[u].append((v, t))
            graph[v].append((u, t))

        shortest_ways = self.dijkstra(n, graph, n - 1)
        counts : List[int] = [-1] * n
        counts[n - 1] = 1

        self.dfs(shortest_ways, counts, 0, MOD)
        
        return counts[0]
