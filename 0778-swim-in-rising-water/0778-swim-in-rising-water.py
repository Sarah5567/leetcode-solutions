class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
            n = len(grid)
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
        
            dist = [[float('inf')] * n for _ in range(n)]
            dist[0][0] = grid[0][0]
        
            heap = [(grid[0][0], 0, 0)]
        
            while heap:
                max_so_far, i, j = heapq.heappop(heap)
                
                if (i, j) == (n - 1, n - 1):
                    return max_so_far
                
                if max_so_far > dist[i][j]:
                    continue
                
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    
                    if 0 <= ni < n and 0 <= nj < n:
                        new_cost = max(max_so_far, grid[ni][nj])
                        
                        if new_cost < dist[ni][nj]:
                            dist[ni][nj] = new_cost
                            heapq.heappush(heap, (new_cost, ni, nj))
            
            return -1