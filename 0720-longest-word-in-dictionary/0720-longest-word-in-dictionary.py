class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            idx = ord(ch) - ord('a')
            if not node.children[idx]:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.is_end = True

    def find_longest(self, node, char: str) -> str:
        if node != self.root and not node.is_end:
            return ""

        longest = ""

        for i in range(26):
            child = node.children[i]
            if child:
                curr =  self.find_longest(child, chr(i + ord('a')))

                if len(curr) > len(longest):
                    longest = curr

        return char + longest


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)

        return trie.find_longest(trie.root, "")