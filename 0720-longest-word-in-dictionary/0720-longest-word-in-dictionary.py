class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def find_longest(self, node, char: str) -> str:
        if node != self.root and not node.is_end:
            return ""

        longest = ""

        for ch, child in node.children.items():
            if child:
                curr =  self.find_longest(child, ch)

            if len(curr) > len(longest) or (len(curr) == len(longest) and curr < longest):
                    longest = curr

        return char + longest


class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        for word in words:
            trie.insert(word)

        return trie.find_longest(trie.root, "")