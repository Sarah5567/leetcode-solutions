class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort(key=lambda word: len(word))
        valid_words = set()
        valid_words.add("")
        longest = ""

        for word in words:
            if word[:-1] in valid_words:
                valid_words.add(word)
                if len(word) > len(longest) or (len(word) == len(longest) and word < longest):
                    longest = word

        return longest
