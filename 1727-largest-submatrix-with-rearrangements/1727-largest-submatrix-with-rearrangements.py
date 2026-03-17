class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        for i in range(1, m):
            for j in range(n):
                matrix[i][j] = (matrix[i - 1][j] + 1) * matrix[i][j]

        lergest_submatrix = 0
        for i in range(m):
            matrix[i].sort(reverse=True)
            for j in range(n):
                if not matrix[i][j]:
                    break
                lergest_submatrix = max(lergest_submatrix, (j + 1) * matrix[i][j])

        return lergest_submatrix
