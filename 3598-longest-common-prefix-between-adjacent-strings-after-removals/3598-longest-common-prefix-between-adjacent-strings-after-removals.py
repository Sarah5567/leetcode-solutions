class Solution:
    def prefix(self, s1 : str, s2 : str, begin : int = 0) -> int:
        length = begin

        for i1, i2 in zip(range(begin, len(s1)), range(begin, len(s2))):
            if s1[i1] != s2[i2]:
                break
            length += 1

        return length

    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        n = len(words)
        max_lcp, second_max_lcp = 0, 0
        max_lcp_index = 0

        res = [0] * n
        prev = -1

        for i in range(1, n):

            length = self.prefix(words[i - 1], words[i])

            if length > max_lcp:
                second_max_lcp = max_lcp
                max_lcp = length
                max_lcp_index = i
            else:
                second_max_lcp = max(second_max_lcp, length)

            if prev == length:
                res[i - 1] = self.prefix(words[i - 2], words[i], begin = length)

            prev = length

        max_lcp_indexes = {max_lcp_index, max_lcp_index - 1}

        for i in range(n):
            res[i] = max(
                res[i],
                second_max_lcp if i in max_lcp_indexes else max_lcp
            )

        return res
