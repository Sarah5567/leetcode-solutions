class Solution:
    def longestPalindrome(self, s: str) -> str:
        ms = '#'
        for ch in s:
            ms += ch + '#'

        n = len(ms)
        p = [0] * n
        l = r = 0

        for i in range(n):
            mirror = l + r - i

            if i < r:
                p[i] = min(r - i, p[mirror])

            while i + p[i] + 1 < n and i - p[i] - 1 >= 0 and \
                  ms[i + p[i] + 1] == ms[i - p[i] - 1]:
                p[i] += 1

            if i + p[i] > r:
                l = i - p[i]
                r = i + p[i]

        longest = 0
        for i in range(n):
            if p[i] > p[longest]:
                longest = i

        start = (longest - p[longest]) // 2
        return s[start:start + p[longest]]
