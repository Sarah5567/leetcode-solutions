class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]
        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        def dfs(r, c, pr, pc):
            visited[r][c] = True
            val = grid[r][c]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc

                if not (0 <= nr < m and 0 <= nc < n):
                    continue

                if grid[nr][nc] != val:
                    continue

                if nr == pr and nc == pc:
                    continue

                if visited[nr][nc]:
                    return True

                if dfs(nr, nc, r, c):
                    return True

            return False

        for r in range(m):
            for c in range(n):
                if not visited[r][c]:
                    if dfs(r, c, -1, -1):
                        return True

        return False
