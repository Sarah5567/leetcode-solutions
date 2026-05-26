class Solution:
    def maxSubstrings(self, word: str) -> int:
        n = len(word)
        prev_index = defaultdict(list)
        cur_end = -1
        count_substrings = 0

        for idx, ch in enumerate(word):
            start = -1
            for i in range(min(len(prev_index[ch]), 3)):
                if idx - prev_index[ch][-i - 1] >= 3:
                    start = prev_index[ch][-i - 1]
                    break

            if start > cur_end:
                cur_end = idx
                count_substrings += 1

            prev_index[ch].append(idx)

        return count_substrings
