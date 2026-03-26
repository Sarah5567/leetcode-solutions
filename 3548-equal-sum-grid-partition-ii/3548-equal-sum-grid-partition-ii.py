class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        
        def check_partition(part_sum, other_sum, current_counter, rows, cols, ends):
            if part_sum == other_sum:
                return True
            diff = part_sum - other_sum
            if diff <= 0 or current_counter.get(diff, 0) == 0:
                return False
            
            if rows > 1 and cols > 1:
                return True
            return diff in ends

        def check_orientation(matrix) -> bool:
            r, c = len(matrix), len(matrix[0])
            
            flat_matrix = list(itertools.chain.from_iterable(matrix))
            top_counter = Counter()
            bottom_counter = Counter(flat_matrix)
            
            top_sum = 0
            bottom_sum = sum(flat_matrix)
            
            for i in range(r - 1):
                row = matrix[i]
                row_sum = sum(row)
                
                for val in row:
                    top_counter[val] += 1
                    bottom_counter[val] -= 1
                
                top_sum += row_sum
                bottom_sum -= row_sum
                
                top_ends = {matrix[0][0], matrix[0][c-1], matrix[i][0], matrix[i][c-1]}
                if check_partition(top_sum, bottom_sum, top_counter, i + 1, c, top_ends):
                    return True
                
                bottom_ends = {matrix[i+1][0], matrix[i+1][c-1], matrix[r-1][0], matrix[r-1][c-1]}
                if check_partition(bottom_sum, top_sum, bottom_counter, r - i - 1, c, bottom_ends):
                    return True
                    
            return False

        if check_orientation(grid):
            return True
            
        transposed_grid = [list(col) for col in zip(*grid)]
        
        return check_orientation(transposed_grid)