class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])

        ans = [['.'] * m for _ in range(n)]

        for i in range(m):
            bottom = n - 1

            for j in range(n-1, -1, -1):
                if boxGrid[i][j] == '*':
                    bottom = j

                if boxGrid[i][j] != '.':
                    ans[bottom][m - 1 - i] = boxGrid[i][j]
                    bottom -= 1

        return ans
