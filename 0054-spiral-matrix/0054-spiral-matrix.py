class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        first_r = 0
        last_r = m - 1
        first_c = 0
        last_c = n - 1

        ans = []

        while first_r <= last_r and first_c <= last_c:
            for i in range(first_c, last_c + 1):
                ans.append(matrix[first_r][i])
            first_r += 1

            for i in range(first_r, last_r + 1):
                ans.append(matrix[i][last_c])
            last_c -= 1

            if first_r > last_r or first_c > last_c:
                break

            for i in range(last_c, first_c - 1, -1):
                ans.append(matrix[last_r][i])
            last_r -= 1

            for i in range(last_r, first_r - 1, -1):
                ans.append(matrix[i][first_c])
            first_c += 1

        return ans
            