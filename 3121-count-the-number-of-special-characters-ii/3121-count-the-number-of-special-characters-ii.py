class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        LETTERS = 26
        lowercase = [-1] * LETTERS
        uppercase = [-1] * LETTERS

        for i, ch in enumerate(word):
            if ch.islower():
                lowercase[ord(ch) - ord('a')] = i
            elif uppercase[ord(ch) - ord('A')] == -1:
                uppercase[ord(ch) - ord('A')] = i

        count = 0
        for i in range(LETTERS):
            if lowercase[i] < uppercase[i] and lowercase[i] != -1:
                count += 1

        return count
