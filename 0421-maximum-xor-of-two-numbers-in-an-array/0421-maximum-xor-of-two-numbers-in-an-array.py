class TrieNode:
    def __init__(self):
        self.children = [None, None]

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = TrieNode()

        for num in nums:
            node = root
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                if not node.children[bit]:
                    node.children[bit] = TrieNode()
                node = node.children[bit]

        max_xor = 0
        for num in nums:
            node = root
            cur_xor = 0
            for i in range(31, -1, -1):
                bit = (num >> i) & 1
                toggled = 1 - bit

                if node.children[toggled]:
                    cur_xor |= (1 << i)
                    node = node.children[toggled]
                else:
                    node = node.children[bit]

            max_xor = max(max_xor, cur_xor)

        return max_xor
