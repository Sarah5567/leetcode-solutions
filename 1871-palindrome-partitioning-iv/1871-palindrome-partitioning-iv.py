class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)

        is_palindrome = [[True] * (n + 1)  for _ in range(n + 1)]

        for length in range(1, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    is_palindrome[i][j] = length <= 2 or is_palindrome[i + 1][j - 1]
                else:
                    is_palindrome[i][j] = False

        for i in range(1, n - 1):
            for j in range(i, n - 1):
                if is_palindrome[0][i - 1] and is_palindrome[i][j] and is_palindrome[j + 1][n - 1]:
                    return True

        return False