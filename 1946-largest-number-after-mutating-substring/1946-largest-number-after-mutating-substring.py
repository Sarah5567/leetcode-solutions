class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        n = len(num)

        l = 0
        while l < n and (d := ord(num[l]) - 48) >= change[d]:
            l += 1

        if l == n:
            return num

        r = l
        while r < n and (d := ord(num[r]) - 48) <= change[d]:
            r += 1

        new_substring = ''.join(
            str(change[ord(c) - 48])
            for c in num[l:r]
        )

        return num[:l] + new_substring + num[r:]