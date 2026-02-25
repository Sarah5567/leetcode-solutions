class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        def sort_string_linear(s: str) -> str:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            result = []
            for i in range(26):
                result.append(chr(i + ord('a')) * count[i])
        
            return ''.join(result)

        for s in strs:
            sorted_s = ''.join(sorted(s))
            if sorted_s in anagrams:
                anagrams[sorted_s].append(s)
            else:
                anagrams[sorted_s] = [s]

        return list(anagrams.values())

