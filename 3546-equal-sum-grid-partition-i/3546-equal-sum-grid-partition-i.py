class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        grid_sum = sum(sum(row) for row in grid)

        upper_sum, lower_sum = 0, grid_sum
        for row in grid:
            row_sum = sum(row)
            upper_sum += row_sum
            lower_sum -= row_sum
            if lower_sum == upper_sum:
                return True

        left_sum, right_sum = 0, grid_sum
        for i in range(len(grid[0])):
            col_sum = sum(row[i] for row in grid)
            left_sum += col_sum
            right_sum -= col_sum
            if left_sum == right_sum:
                return True

        return False