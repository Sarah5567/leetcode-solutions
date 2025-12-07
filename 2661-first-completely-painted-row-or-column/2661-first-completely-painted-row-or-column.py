class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])

        indexes = [-1] * (m * n + 1)
        paintedInRow = [0] * m
        paintedInCol = [0] * n

        for i in range(m):
            for j in range(n):
                indexes[mat[i][j]] = (i, j)

        for i, val in enumerate(arr):
            r, c = indexes[val]
            paintedInRow[r] += 1
            paintedInCol[c] += 1
            if paintedInRow[r] == n or paintedInCol[c] == m:
                return i
        
        return -1