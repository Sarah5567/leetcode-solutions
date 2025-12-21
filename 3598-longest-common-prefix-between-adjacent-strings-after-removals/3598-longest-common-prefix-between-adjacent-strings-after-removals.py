class Solution:
    def prefix(self, s1: str, s2: str, begin: int = 0) -> int:
        limit = min(len(s1), len(s2))
        i = begin

        while i < limit and s1[i] == s2[i]:
            i += 1

        return i

    def longestCommonPrefix(self, words: List[str]) -> List[int]:
        n = len(words)
        max_lcp, second_max_lcp = 0, 0
        max_lcp_index = 0

        res = [0] * n
        prev = -1

        for i in range(1, n):
            length = self.prefix(words[i - 1], words[i])

            if length > max_lcp:
                second_max_lcp, max_lcp = max_lcp, length
                max_lcp_index = i
            else:
                second_max_lcp = max(second_max_lcp, length)

            if prev == length:
                res[i - 1] = self.prefix(words[i - 2], words[i], begin=length)

            prev = length

        for i in range(n):
            candidate = second_max_lcp if i == max_lcp_index or i == max_lcp_index - 1 else max_lcp
            res[i] = max(res[i], candidate)

        return res
