class Solution:
    def maxSubstrings(self, word: str) -> int:
        n = len(word)
        prev_index = defaultdict(list)
        start = [-1] * n

        for idx, ch in enumerate(word):
            for i in range(min(len(prev_index[ch]), 3)):
                if idx - prev_index[ch][-i - 1] >= 3:
                    start[idx] = prev_index[ch][-i - 1]
                    break

            prev_index[ch].append(idx)

        cur_end = -1
        count_substrings = 0
        for i in range(n):
            if start[i] > cur_end:
                cur_end = i
                count_substrings += 1

        return count_substrings
        