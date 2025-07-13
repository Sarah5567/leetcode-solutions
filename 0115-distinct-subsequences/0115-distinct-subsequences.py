class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        count = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]
        for i in range(len(s) + 1):
            count[0][i] = 1
        for i in range(1, len(t) + 1):
            for j in range(1, len(s) + 1):
                if t[i - 1] == s[j - 1]:
                    count[i][j] = (count[i - 1][j - 1] + count[i][j - 1])
                else:
                    count[i][j] = count[i][j - 1]
        return count[len(t)][len(s)]
