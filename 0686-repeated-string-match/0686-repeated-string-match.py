class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeats = (len(b) + len(a) - 1) // len(a)

        s = a * repeats
        if b in s:
            return repeats

        s += a
        if b in s:
            return repeats + 1

        return -1
