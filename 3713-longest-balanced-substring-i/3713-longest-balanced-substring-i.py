class Solution:
    def longestBalanced(self, s: str) -> int:
        ALPHABET_SIZE : int = 26
        n : int = len(s)

        alpha_freq : List[int] = [0] * ALPHABET_SIZE
        freq_count : List[int] = [0] * (n + 1)

        longest : int = 0

        for i in range(n):
            for j in range(i, n):
                alpha_index : int = ord(s[j]) - ord('a')

                freq_count[alpha_freq[alpha_index]] -= 1
                alpha_freq[alpha_index] += 1
                freq_count[alpha_freq[alpha_index]] += 1

                if j - i + 1 == alpha_freq[alpha_index] * freq_count[alpha_freq[alpha_index]]:
                    longest = max(longest, j - i + 1)

            alpha_freq = [0] * ALPHABET_SIZE
            freq_count = [0] * (n + 1)

        return longest