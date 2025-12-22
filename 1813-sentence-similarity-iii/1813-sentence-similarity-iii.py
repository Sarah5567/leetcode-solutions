class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        w1 = sentence1.split()
        w2 = sentence2.split()

        # Ensure w1 is the shorter one
        if len(w1) > len(w2):
            w1, w2 = w2, w1

        i = 0
        # Match prefix
        while i < len(w1) and w1[i] == w2[i]:
            i += 1

        j = 0
        # Match suffix
        while j < len(w1) - i and w1[-1 - j] == w2[-1 - j]:
            j += 1

        return i + j == len(w1)
