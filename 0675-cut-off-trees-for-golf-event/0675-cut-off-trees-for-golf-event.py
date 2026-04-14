class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        if not forest or not forest[0]:
            return -1
        
        m, n = len(forest), len(forest[0])
        
        trees = []
        for i in range(m):
            for j in range(n):
                if forest[i][j] > 1:
                    trees.append((forest[i][j], i, j))
        trees.sort()
        
        def bfs(sx, sy, tx, ty):
            if sx == tx and sy == ty:
                return 0
            
            visited = [[False]*n for _ in range(m)]
            q = deque([(sx, sy, 0)])
            visited[sx][sy] = True
            
            while q:
                x, y, d = q.popleft()
                for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and forest[nx][ny] != 0:
                        if nx == tx and ny == ty:
                            return d + 1
                        visited[nx][ny] = True
                        q.append((nx, ny, d + 1))
            return -1
        
        cx, cy = 0, 0
        total_steps = 0
        
        for _, tx, ty in trees:
            dist = bfs(cx, cy, tx, ty)
            if dist == -1:
                return -1
            total_steps += dist
            cx, cy = tx, ty
        
        return total_steps
