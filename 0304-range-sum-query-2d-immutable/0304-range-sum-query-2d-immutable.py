class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])

        self.sums = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                self.sums[i + 1][j + 1] = self.sums[i][j + 1] + self.sums[i + 1][j] - self.sums[i][j] + matrix[i][j]
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        height = row2 - row1 + 1
        width = col2 - col1 + 1

        ans = self.sums[row2 + 1][col2 + 1] 
        ans -= self.sums[row2 + 1 - height][col2 + 1] + self.sums[row2 + 1][col2 + 1 - width] 
        ans += self.sums[row2 + 1 - height][col2 + 1 - width]

        return ans
        