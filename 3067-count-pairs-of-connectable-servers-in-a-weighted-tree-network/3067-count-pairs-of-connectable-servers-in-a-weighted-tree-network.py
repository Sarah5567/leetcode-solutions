class Solution:
    def countPairsOfConnectableServers(self, edges: List[List[int]], signalSpeed: int) -> List[int]:
        def count_divisible_descendants(graph, u, parent, dist) -> int:
            count = 1 if dist % signalSpeed == 0 else 0
            for v, w in graph[u]:
                if v != parent:
                    count += count_divisible_descendants(graph, v, u, dist + w)
            return count

        n = max(max(u, v) for u, v, w in edges) + 1
        graph = [[] for _ in range(n)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

        res = [0] * n
        for u in range(n):
            counts = [count_divisible_descendants(graph, v, u, w) for v, w in graph[u]]
            res[u] = sum(counts[i] * counts[j] for i in range(len(counts)) for j in range(i + 1, len(counts)))

        return res
        