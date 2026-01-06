class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        n = len(s)
        ALPHABET_SIZE = 26

        letter_positions = defaultdict(list)
        for i, ch in enumerate(s):
            letter_positions[ord(ch) - ord('a')].append(i)

        letter_prefix_counts = [[0] * n for _ in range(ALPHABET_SIZE)]

        for letter, positions in letter_positions.items():
            letter_prefix_counts[letter][0] = 1 if positions and positions[0] == 0 else 0
            idx = letter_prefix_counts[letter][0]

            for i in range(1, n):
                letter_prefix_counts[letter][i] = letter_prefix_counts[letter][i - 1]
                if idx < len(positions) and positions[idx] == i:
                    letter_prefix_counts[letter][i] += 1
                    idx += 1

        count_palindromes = 0
        for outer_letter, positions in letter_positions.items():
            if len(positions) < 2:
                continue

            left = positions[0] + 1
            right = positions[-1] - 1
            if left > right:
                continue

            count_mid_options = 0
            for mid_letter in letter_positions:
                if (
                    letter_prefix_counts[mid_letter][right]
                    > letter_prefix_counts[mid_letter][left - 1]
                ):
                    count_mid_options += 1

            count_palindromes += count_mid_options

        return count_palindromes
