class Solution:
    def doesAliceWin(self, s: str) -> bool:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        return any(char in vowels for char in s)
