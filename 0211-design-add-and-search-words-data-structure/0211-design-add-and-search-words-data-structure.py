class WordDictionary:

    def __init__(self):
        self.children = {}
        self.is_end = False

    def addWord(self, word: str, idx = 0) -> None:
        if idx == len(word):
            self.is_end = True
        else:
            letter = ord(word[idx]) - ord('a')
            if not letter in self.children:
                self.children[letter] = WordDictionary()
            self.children[letter].addWord(word, idx + 1)

    def search(self, word: str, idx = 0) -> bool:
        if idx == len(word):
            return self.is_end
        else:
            if word[idx] == '.':
                for dictionary in self.children.values():
                    if dictionary.search(word, idx + 1):
                        return True
                return False
            else:
                letter = ord(word[idx]) - ord('a')
                return letter in self.children and self.children[letter].search(word, idx + 1)
