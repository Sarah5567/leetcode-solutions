class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows, cols = len(matrix), len(matrix[0])
        ans = 0
        
        prefix_rows = [[0] * (cols + 1) for _ in range(rows)]
        for r in range(rows):
            for c in range(cols):
                prefix_rows[r][c+1] = prefix_rows[r][c] + matrix[r][c]

        for left in range(cols):
            for right in range(left, cols):
                count = defaultdict(int)
                count[0] = 1
                curr_sum = 0

                for r in range(rows):
                    curr_sum += prefix_rows[r][right+1] - prefix_rows[r][left]
                    ans += count[curr_sum - target]
                    count[curr_sum] += 1

        return ans
