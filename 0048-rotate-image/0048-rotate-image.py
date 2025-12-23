class Solution:
    def new_pos(self, n : int, row : int, col : int) -> Tuple[int, int]:
        return col, n - row - 1

    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(int(n / 2)):
            for j in range(i, n - i - 1):
                next_r, next_c = i, j
                val = matrix[next_r][next_c]

                for _ in range(4):
                    cur_r, cur_c = next_r, next_c
                    next_r, next_c = self.new_pos(n, cur_r, cur_c)
                    val, matrix[next_r][next_c] = matrix[next_r][next_c], val
