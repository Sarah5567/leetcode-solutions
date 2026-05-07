class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m = len(board)
        n = len(board[0])

        trie = Trie()
        for word in words:
            trie.insert(word)

        ans = []
        visited = [[False] * n for _ in range(m)]

        def dfs(r, c, trie_node, cur_word):
            visited[r][c] = True

            if trie_node.is_end:
                ans.append(cur_word)
                trie_node.is_end = False

            neighbors = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

            for nr, nc in neighbors:
                if nr in [-1, m] or nc in [-1, n] or visited[nr][nc]:
                    continue

                if board[nr][nc] in trie_node.children:
                    dfs(nr, nc, trie_node.children[board[nr][nc]], cur_word + board[nr][nc])

            visited[r][c] = False

        for i in range(m):
            for j in range(n):
                if board[i][j] in trie.root.children:
                    dfs(i, j, trie.root.children[board[i][j]], board[i][j])

        return ans
