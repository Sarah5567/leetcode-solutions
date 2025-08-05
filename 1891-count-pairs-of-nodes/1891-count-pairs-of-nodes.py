from collections import defaultdict
from bisect import bisect_right

class Solution:
    def countPairs(self, n: int, edges: List[List[int]], queries: List[int]) -> List[int]:
        degree = [0] * (n + 1)
        shared = defaultdict(int)

        for u, v in edges:
            if u > v:
                u, v = v, u
            degree[u] += 1
            degree[v] += 1
            shared[(u, v)] += 1

        sorted_deg = sorted(degree[1:])
        result = []

        for q in queries:
            count = 0
            i, j = 0, n - 1

            while i < j:
                if sorted_deg[i] + sorted_deg[j] <= q:
                    i+=1
                else:
                    count += (j - i)
                    j -= 1
                
            
            for (u, v), freq in shared.items():
                if degree[u] + degree[v] > q and degree[u] + degree[v] - freq <= q:
                    count -= 1
            
            result.append(count)
            
        return result
