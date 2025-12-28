class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        mod = 1000000007
        alphabet_size = 26
        word_len = len(words[0])
        target_len = len(target)

        letters_per_idx = [[0] * word_len for _ in range(alphabet_size)]
        for word in words:
            for i, ch in enumerate(word):
                letters_per_idx[ord(ch) - ord('a')][i] += 1

        dp = [[0] * (word_len + 1) for _ in range(target_len + 1)]
        for i in range(word_len + 1):
            dp[0][i] = 1

        for i in range(1, target_len + 1):
            target_letter = ord(target[i - 1]) - ord('a')
            for j in range(i, word_len + 1 - (target_len - i)):
                dp[i][j] = (dp[i][j - 1] + (letters_per_idx[target_letter][j - 1] * dp[i - 1][j - 1] % mod)) % mod

        return dp[target_len][word_len]