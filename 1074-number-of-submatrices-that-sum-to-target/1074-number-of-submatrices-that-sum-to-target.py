class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        ans = 0

        for left in range(cols):
            row_sum = [0] * rows

            for right in range(left, cols):

                for r in range(rows):
                    row_sum[r] += matrix[r][right]

                prefix = 0
                count = defaultdict(int)
                count[0] = 1

                for val in row_sum:
                    prefix += val
                    ans += count[prefix - target]
                    count[prefix] += 1

        return ans