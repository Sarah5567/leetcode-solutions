class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def is_valid_cell(r: int, c: int) -> bool:
            return r < m and r >= 0 and c < n and c >= 0

        def dfs(r: int, c: int, source) -> bool:
            visited[r][c] = True

            neighbors = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]

            for r_neighbor, c_neighbor in neighbors:
                if not is_valid_cell(r_neighbor, c_neighbor):
                    continue

                if not grid[r_neighbor][c_neighbor] == grid[r][c]:
                    continue

                if (r_neighbor, c_neighbor) == source:
                    continue

                if visited[r_neighbor][c_neighbor] or dfs(r_neighbor, c_neighbor, (r, c)):
                    return True
                        
            return False

        for r in range(m):
            for c in range(n):
                if not visited[r][c] and dfs(r, c, (-1, -1)):
                    return True

        return False