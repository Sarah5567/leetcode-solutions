class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        # local bindings for speed
        width = [[0] * n for _ in range(m)]
        matrix0 = matrix[0]

        # compute consecutive widths
        for i in range(m):
            row = matrix[i]
            w = width[i]
            w[0] = 1 if row[0] == '1' else 0
            for j in range(1, n):
                if row[j] == '1':
                    w[j] = w[j - 1] + 1
                else:
                    w[j] = 0

        # compute up-span
        up = [[0] * n for _ in range(m)]
        for j in range(n):
            stack = []
            for i in range(m):
                cur_width = width[i][j]
                while stack and width[stack[-1]][j] > cur_width:
                    stack.pop()

                up[i][j] = i + 1 if not stack else i - stack[-1]
                stack.append(i)

        # compute down-span
        down = [[0] * n for _ in range(m)]
        for j in range(n):
            stack = []
            for i in range(m - 1, -1, -1):
                cur_width = width[i][j]
                while stack and width[stack[-1]][j] >= cur_width:
                    stack.pop()

                down[i][j] = (m - i) if not stack else (stack[-1] - i)
                stack.append(i)

        # compute maximal rectangle
        maxRect = 0
        for i in range(m):
            w_row = width[i]
            up_row = up[i]
            down_row = down[i]
            for j in range(n):
                h = up_row[j] + down_row[j] - 1
                area = w_row[j] * h
                if area > maxRect:
                    maxRect = area

        return maxRect
