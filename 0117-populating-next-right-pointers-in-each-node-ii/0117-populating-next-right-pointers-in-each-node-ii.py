"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None

        queue = deque()
        queue.appendleft(root)
        queue.appendleft(None)

        while len(queue) > 1:
            node = queue.pop()

            if not node:
                queue.appendleft(None)
                continue

            node.next = queue[-1]

            if node.left:          
                queue.appendleft(node.left)
            if node.right:          
                queue.appendleft(node.right)

        return root
