class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        count_x = [[0] * n for _ in range(m)]
        count_y = [[0] * n for _ in range(m)]
        count_x[0][0] = (grid[0][0] == 'X')
        count_y[0][0] = (grid[0][0] == 'Y')

        for i in range(1, m):
            count_x[i][0] = count_x[i - 1][0] + (grid[i][0] == 'X')
            count_y[i][0] = count_y[i - 1][0] + (grid[i][0] == 'Y')
            if count_x[i][0] == count_y[i][0] and count_x[i][0]:
                count += 1

        for i in range(1, n):
            count_x[0][i] = count_x[0][i - 1] + (grid[0][i] == 'X')
            count_y[0][i] = count_y[0][i - 1] + (grid[0][i] == 'Y')
            if count_x[0][i] == count_y[0][i] and count_x[0][i]:
                count += 1

        for i in range(1, m):
            for j in range(1, n):
                count_x[i][j] = count_x[i - 1][j] + count_x[i][j - 1] - count_x[i - 1][j - 1] + (grid[i][j] == 'X')
                count_y[i][j] = count_y[i - 1][j] + count_y[i][j - 1] - count_y[i - 1][j - 1] + (grid[i][j] == 'Y')
                if count_x[i][j] == count_y[i][j] and count_x[i][j]:
                    count += 1

        return count