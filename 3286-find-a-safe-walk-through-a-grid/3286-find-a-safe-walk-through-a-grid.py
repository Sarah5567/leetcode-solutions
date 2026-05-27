class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        q.append((0,0))

        next_q = deque()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        visited = [[False] * n for _ in range(m)]
        visited[0][0] = True

        for _ in range(grid[0][0], health):
            while q:
                r, c = q.popleft()

                if r == m - 1 and c == n - 1:
                    return True

                for x, y in directions:
                    next_r = r + x
                    next_c = c + y

                    if not ((0 <= next_r < m) and (0 <= next_c < n)):
                        continue
                    if visited[next_r][next_c]:
                        continue

                    visited[next_r][next_c] = True

                    if not grid[next_r][next_c]:
                        if next_r == m - 1 and next_c == n-1:
                            return True

                        q.append((next_r, next_c))
                    else:
                        next_q.append((next_r, next_c))

            q = next_q
            next_q = deque()

        return False
