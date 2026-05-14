class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(row, col, index):
            if index == len(word) - 1:
                return True

            neighbors = [(row + 1, col), (row, col + 1), (row - 1, col), (row, col - 1)]

            for nr, nc in neighbors:
                if nr == m or nr < 0 or nc == n or nc < 0:
                    continue

                if board[nr][nc] != word[index + 1]:
                    continue

                if visited[nr][nc]:
                    continue

                visited[nr][nc] = True
                if dfs(nr, nc, index + 1):
                    return True
                visited[nr][nc] = False

            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if dfs(i, j, 0):
                        return True
                    visited[i][j] = False

        return False
