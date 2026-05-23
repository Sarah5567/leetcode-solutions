class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        l = 0
        while l < len(num) and int(num[l]) >= change[int(num[l])]:
            l += 1

        if l == len(num):
            return num

        r = l
        while r < len(num) and int(num[r]) <= change[int(num[r])]:
            r += 1


        new_substring = ''.join(str(change[int(c)]) for c in num[l:r])

        return num[:l] + new_substring + num[r:]
