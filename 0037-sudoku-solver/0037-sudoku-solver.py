from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.board = board
        self.rows = [set() for _ in range(9)]
        self.cols = [set() for _ in range(9)]
        self.boxes = [set() for _ in range(9)]

        # Pre-fill sets with existing values
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    self.rows[r].add(val)
                    self.cols[c].add(val)
                    self.boxes[(r // 3) * 3 + (c // 3)].add(val)

        self.fillSudoku(0, 0)

    def fillSudoku(self, row: int, col: int) -> bool:
        if row == 9:
            return True
        next_row, next_col = (row + 1, 0) if col == 8 else (row, col + 1)

        if self.board[row][col] != '.':
            return self.fillSudoku(next_row, next_col)

        box_idx = (row // 3) * 3 + (col // 3)
        for i in range(1, 10):
            val = str(i)
            if val not in self.rows[row] and val not in self.cols[col] and val not in self.boxes[box_idx]:
                self.board[row][col] = val
                self.rows[row].add(val)
                self.cols[col].add(val)
                self.boxes[box_idx].add(val)

                if self.fillSudoku(next_row, next_col):
                    return True

                self.board[row][col] = '.'
                self.rows[row].remove(val)
                self.cols[col].remove(val)
                self.boxes[box_idx].remove(val)

        return False
