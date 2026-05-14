class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        m = len(board)
        n = len(board[0])

        def get_indexes(num):
            num -= 1
            row = num // n
            col = num % n
            if row % 2:
                col = n - 1 - col
            row = m - 1 - row
            return row, col

        q = deque()
        shortest = [[-1] * n for _ in range(m)]
        q.append(1)

        first_r, first_c = get_indexes(1)
        dest_r, dest_c = get_indexes(m * n)

        shortest[first_r][first_c] = 0

        while shortest[dest_r][dest_c] == -1 and q:
            cell = q.popleft()
            r, c = get_indexes(cell)
            for i in range(cell + 1, min(cell + 6, m * n) + 1):
                next_cell = i
                next_r, next_c = get_indexes(next_cell)
                if board[next_r][next_c] != -1:
                    next_cell = board[next_r][next_c]
                    next_r, next_c = get_indexes(next_cell)

                if shortest[next_r][next_c] == -1:
                    shortest[next_r][next_c] = shortest[r][c] + 1
                    q.append(next_cell)

        return shortest[dest_r][dest_c]
