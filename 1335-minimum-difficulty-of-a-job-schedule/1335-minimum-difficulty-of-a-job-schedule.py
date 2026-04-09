class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        n = len(jobDifficulty)

        if n < d:
            return -1

        dp = [[0] * n for _ in range(d)]

        dp[0][0] = jobDifficulty[0]
        for i in range(1, n):
            dp[0][i] = max(dp[0][i - 1], jobDifficulty[i])

        for day in range(1, d):
            for i in range(day, n):
                difficulty = jobDifficulty[i]
                dp[day][i] = difficulty + dp[day - 1][i - 1]

                for j in range(i - 1, day - 1, -1):
                    difficulty = max(difficulty, jobDifficulty[j])
                    dp[day][i] = min(dp[day][i], difficulty + dp[day - 1][j - 1])

        return dp[-1][-1]
