class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [True] * n
        prev_dp = [True] * n
        count = n

        for length in range(2, n + 1):
            next_dp = [False] * n
            for i in range(length - 1, n):
                if s[i] == s[i - length + 1] and prev_dp[i - 1]:
                    next_dp[i] = True
                    count += 1

            dp, prev_dp = next_dp, dp
         
        return count