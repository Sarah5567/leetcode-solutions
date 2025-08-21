class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        full_mask = (1 << len(graph)) - 1
        queue = deque()
        visited = set()
        
        for i in range(len(graph)):
            mask = 1 << i
            queue.append((i, mask, 0))
            visited.add((i, mask))
            
        while queue:
            node, mask, steps = queue.popleft()
            
            if mask == full_mask:
                return steps
                
            for neighbor in graph[node]:
                new_mask = mask | 1 << neighbor
                if not (neighbor, new_mask) in visited:
                    queue.append((neighbor, new_mask, steps + 1))
                    visited.add((neighbor, new_mask))
                    
        return -1