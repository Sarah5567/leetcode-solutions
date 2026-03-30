class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        even = [0] * 26
        odd = [0] * 26

        for i, (c1, c2) in enumerate(zip(s1, s2)):
            idx1 = ord(c1) - ord('a')
            idx2 = ord(c2) - ord('a')

            if i % 2 == 0:
                even[idx1] += 1
                even[idx2] -= 1
            else:
                odd[idx1] += 1
                odd[idx2] -= 1

        return even == [0] * 26 and odd == [0] * 26
