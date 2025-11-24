class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])

        width = [[0] * n for _ in range(m)]

        # compute consecutive widths
        for i in range(m):
            width[i][0] = int(matrix[i][0])
            for j in range(1, n):
                width[i][j] = width[i][j - 1] + 1  if matrix[i][j] == '1' else 0

        # compute up-span
        up = [[0] * n for _ in range(m)]
        for j in range(n):
            stack = []
            for i in range(m):
                while stack and width[stack[-1]][j] > width[i][j]:
                    stack.pop()

                up[i][j] = i + 1 if not stack else i - stack[-1]

                stack.append(i)

        # compute down-span
        down = [[0] * n for _ in range(m)]
        for j in range(n):
            stack = []
            for i in range(m - 1, -1, -1):
                while stack and width[stack[-1]][j] >= width[i][j]:
                    stack.pop()

                down[i][j] = (m - i) if not stack else (stack[-1] - i)

                stack.append(i)

        # compute maximal rectangle
        maxRect = 0
        for i in range(m):
            for j in range(n):
                height = up[i][j] + down[i][j] - 1
                maxRect = max(maxRect, width[i][j] * height)

        return maxRect
