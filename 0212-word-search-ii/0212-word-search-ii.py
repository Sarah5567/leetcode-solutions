class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]

        node.is_end = True


class Solution:
    def findWords(self, board, words):
        m, n = len(board), len(board[0])

        trie = Trie()

        for word in words:
            trie.insert(word)

        ans = []

        def dfs(r, c, node, cur_word):
            char = board[r][c]

            if node.is_end:
                ans.append(cur_word)
                node.is_end = False

            board[r][c] = "#"

            if r > 0:
                nxt = board[r - 1][c]
                if nxt in node.children:
                    dfs(r - 1, c, node.children[nxt], cur_word + nxt)

            if r < m - 1:
                nxt = board[r + 1][c]
                if nxt in node.children:
                    dfs(r + 1, c, node.children[nxt], cur_word + nxt)

            if c > 0:
                nxt = board[r][c - 1]
                if nxt in node.children:
                    dfs(r, c - 1, node.children[nxt], cur_word + nxt)

            if c < n - 1:
                nxt = board[r][c + 1]
                if nxt in node.children:
                    dfs(r, c + 1, node.children[nxt], cur_word + nxt)

            board[r][c] = char

        root_children = trie.root.children

        for i in range(m):
            for j in range(n):
                char = board[i][j]

                if char in root_children:
                    dfs(i, j, root_children[char], char)

        return ans