class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        
        flat_grid = list(itertools.chain.from_iterable(grid))
        total_sum = sum(flat_grid)
        base_counter = Counter(flat_grid)

        def check_partition(part_sum, other_sum, current_counter, rows, cols, ends):
            if part_sum == other_sum:
                return True
            diff = part_sum - other_sum
            if diff <= 0 or current_counter.get(diff, 0) == 0:
                return False
            
            if rows > 1 and cols > 1:
                return True
            return diff in ends

        top_counter = Counter()
        bottom_counter = base_counter.copy()
        top_sum = 0
        bottom_sum = total_sum
        
        for i in range(m - 1):
            row = grid[i]
            row_sum = sum(row)
            
            for val in row:
                top_counter[val] += 1
                bottom_counter[val] -= 1
            
            top_sum += row_sum
            bottom_sum -= row_sum
            
            top_ends = {grid[0][0], grid[0][n-1], grid[i][0], grid[i][n-1]}
            if check_partition(top_sum, bottom_sum, top_counter, i + 1, n, top_ends):
                return True
            
            bottom_ends = {grid[i+1][0], grid[i+1][n-1], grid[m-1][0], grid[m-1][n-1]}
            if check_partition(bottom_sum, top_sum, bottom_counter, m - i - 1, n, bottom_ends):
                return True

        left_counter = Counter()
        right_counter = base_counter.copy()
        left_sum = 0
        right_sum = total_sum
        
        for j in range(n - 1):
            col_sum = 0
            for i in range(m):
                val = grid[i][j]
                col_sum += val
                left_counter[val] += 1
                right_counter[val] -= 1
            
            left_sum += col_sum
            right_sum -= col_sum
            
            left_ends = {grid[0][0], grid[m-1][0], grid[0][j], grid[m-1][j]}
            if check_partition(left_sum, right_sum, left_counter, m, j + 1, left_ends):
                return True
            
            right_ends = {grid[0][j+1], grid[m-1][j+1], grid[0][n-1], grid[m-1][n-1]}
            if check_partition(right_sum, left_sum, right_counter, m, n - j - 1, right_ends):
                return True

        return False
