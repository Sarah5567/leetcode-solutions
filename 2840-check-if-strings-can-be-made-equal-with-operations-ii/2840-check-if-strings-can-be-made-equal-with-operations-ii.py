class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        n = len(s1)
        odd_positions = [0] * 26
        even_positions = [0] * 26

        for i in range(n):
            if i % 2:
                odd_positions[ord(s1[i]) - ord('a')] += 1
                odd_positions[ord(s2[i]) - ord('a')] -= 1
            else:
                even_positions[ord(s1[i]) - ord('a')] += 1
                even_positions[ord(s2[i]) - ord('a')] -= 1

        return all(
            even_positions[i] == 0 and odd_positions[i] == 0
            for i in range(26)
        )
