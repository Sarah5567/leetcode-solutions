class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        letters = ['a', 'b', 'c']

        s = ['a']
        for i in range(1, n):
            for c in letters:
                if c != s[i-1]:
                    s.append(c)
                    break

        def next_happy(s):
            for i in range(len(s) - 1, -1, -1):
                for c in letters:
                    if c > s[i] and (i == 0 or c != s[i-1]):
                        s[i] = c

                        for j in range(i + 1, len(s)):
                            for x in letters:
                                if x != s[j-1]:
                                    s[j] = x
                                    break
                        return True
            return False

        if k == 1:
            return ''.join(s)

        for _ in range(k - 1):
            if not next_happy(s):
                return ""

        return ''.join(s)        