class Solution:
    def longestPalindrome(self, word1: str, word2: str) -> int:
        word = word1 + word2
        n = len(word)

        # Preconvert chars to ints 0–25 to avoid repeated ord() calls
        A = [ord(c) - 97 for c in word]
        A1 = A[:len(word1)]
        A2 = A[len(word1):]

        # DP table
        dp = [[0] * n for _ in range(n)]

        # Length-1 substrings
        for i in range(n):
            dp[i][i] = 1

        # Fill DP for increasing lengths
        for length in range(2, n + 1):
            # cache dp and A locally for speed
            dp_local = dp
            A_local = A

            for l in range(n - length + 1):
                r = l + length - 1

                if A_local[l] == A_local[r]:
                    if length > 2:
                        dp_local[l][r] = dp_local[l + 1][r - 1] + 2
                    else:
                        dp_local[l][r] = 2
                else:
                    # local variables reduce attribute lookups
                    left = dp_local[l + 1][r]
                    right = dp_local[l][r - 1]
                    dp_local[l][r] = left if left >= right else right

        # Collect positions of each letter in word2
        pos_last = [[] for _ in range(26)]
        for j, ch in enumerate(A2):
            pos_last[ch].append(j)

        m = len(word1)
        longest = 0

        # Compare word1 positions to last occurrences in word2
        for i, ch in enumerate(A1):
            lst = pos_last[ch]
            if lst:
                j2 = m + lst[-1]
                if i + 1 <= j2 - 1:
                    val = dp[i + 1][j2 - 1] + 2
                else:
                    val = 2
                if val > longest:
                    longest = val

        return longest
