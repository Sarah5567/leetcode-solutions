class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        ones = [sum(int(ch) for ch in string) for string in strs]

        for k, string in enumerate(strs):
            zeros = len(string) - ones[k]

            for i in range(m, -1, -1):
                for j in range(n, -1, -1):
                        if i + zeros <= m and j + ones[k] <= n:
                            dp[i + zeros][j + ones[k]] = max(dp[i + zeros][j + ones[k]], dp[i][j] + 1)

        return max(max(row) for row in dp)
