class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                board[i][j] += 1

        directions = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

        for i in range(m):
            for j in range(n):
                live_neighbors = 0

                for direction in directions:
                    row = i + direction[0]
                    col = j + direction[1]
                    if row >= 0 and row < m and col >= 0 and col < n and abs(board[row][col]) == 2:
                        live_neighbors += 1

                if board[i][j] == 1 and live_neighbors != 3:
                        board[i][j] = -board[i][j]
                elif board[i][j] == 2 and live_neighbors not in [2, 3]:
                        board[i][j] = -board[i][j]

        for i in range(m):
            for j in range(n):
                board[i][j] = 1 if board[i][j] > 0 else 0
                