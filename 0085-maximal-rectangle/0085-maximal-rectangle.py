class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        # Preallocate
        width = [[0] * n for _ in range(m)]
        up = [[0] * n for _ in range(m)]
        down = [[0] * n for _ in range(m)]

        # ----- compute consecutive widths -----
        for i in range(m):
            row = matrix[i]
            w = width[i]
            prev = 0
            for j in range(n):
                if row[j] == '1':
                    prev += 1
                else:
                    prev = 0
                w[j] = prev

        # ----- compute up-span -----
        for j in range(n):
            stack = []
            col_width = [width[i][j] for i in range(m)]
            col_up = up  # alias for speed

            for i in range(m):
                cur = col_width[i]
                # pop while top width > cur
                while stack and col_width[stack[-1]] > cur:
                    stack.pop()

                col_up[i][j] = i + 1 if not stack else i - stack[-1]
                stack.append(i)

        # ----- compute down-span -----
        for j in range(n):
            stack = []
            col_width = [width[i][j] for i in range(m)]
            col_down = down  # alias for speed

            for i in range(m - 1, -1, -1):
                cur = col_width[i]
                # pop while top width >= cur
                while stack and col_width[stack[-1]] >= cur:
                    stack.pop()

                col_down[i][j] = (m - i) if not stack else (stack[-1] - i)
                stack.append(i)

        # ----- compute maximal rectangle -----
        maxRect = 0
        for i in range(m):
            w_row = width[i]
            up_row = up[i]
            down_row = down[i]
            for j in range(n):
                if w_row[j]:  # quick skip
                    h = up_row[j] + down_row[j] - 1
                    area = w_row[j] * h
                    if area > maxRect:
                        maxRect = area

        return maxRect
