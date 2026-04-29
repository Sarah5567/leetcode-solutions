class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)


        dp = [True] * n
        prev_dp = [True] * n

        longest = s[0]

        for length in range(2, n + 1):
            next_dp = [0] * n
            for i in range(n - length + 1):
                if s[i] == s[i + length - 1] and prev_dp[i + 1]:
                    next_dp[i] = True
                    longest = s[i:i + length]

            prev_dp = dp
            dp = next_dp

        return longest
