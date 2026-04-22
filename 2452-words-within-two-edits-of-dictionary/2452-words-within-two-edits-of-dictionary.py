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

    def dfs(self, node, word, edits = 0, idx = 0):
        if edits > 2:
            return False

        if node.is_end:
            return True

        for ch, child in node.children.items():
            if ch == word[idx] and self.dfs(child, word, edits, idx + 1):
                return True
            elif self.dfs(child, word, edits + 1, idx + 1):
                return True
            
        return False
        
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        ans = []
        for word in queries:
            if trie.dfs(trie.root, word):
                ans.append(word)

        return ans