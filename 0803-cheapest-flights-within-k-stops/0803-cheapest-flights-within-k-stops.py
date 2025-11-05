class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        heap = [(0, src, 0)]
        
        visited = {}
        
        while heap:
            cost, node, stops = heapq.heappop(heap)
            
            if node == dst:
                return cost
            
            if (node, stops) in visited and visited[(node, stops)] <= cost:
                continue
            visited[(node, stops)] = cost
            
            if stops > k:
                continue
            
            for neighbor, price in graph[node]:
                heapq.heappush(heap, (cost + price, neighbor, stops + 1))
        
        return -1
