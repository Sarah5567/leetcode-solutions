class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        word = word1 + word2
        n = len(word)

        # Standard LPS DP: dp[l][r] = longest palindromic subsequence in word[l..r]
        dp = [[0] * n for _ in range(n)]

        # Substrings of length 1
        for i in range(n):
            dp[i][i] = 1

        # Substrings of increasing length
        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1
                if word[l] == word[r]:
                    dp[l][r] = dp[l + 1][r - 1] + 2 if length > 2 else 2
                else:
                    dp[l][r] = max(dp[l + 1][r], dp[l][r - 1])

        # Now check palindromes that start in word1 and end in word2
        m = len(word1)
        longest = 0

        pos_last = [[] for _ in range(26)]
        for j, ch in enumerate(word2):
            pos_last[ord(ch) - ord('a')].append(j)

        for i, ch in enumerate(word1):
            letter = ord(ch) - ord('a')
            if pos_last[letter]:
                # Last occurrence of ch inside word2
                j2 = m + pos_last[letter][-1]
                if i + 1 <= j2 - 1:
                    longest = max(longest, dp[i + 1][j2 - 1] + 2)
                else:
                    longest = max(longest, 2)

        return longest
