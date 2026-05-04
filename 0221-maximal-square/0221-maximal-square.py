class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[int(cell) for cell in row] for row in matrix]

        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] += (min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])) * dp[i][j]

        return max(max(row) for row in dp) ** 2
