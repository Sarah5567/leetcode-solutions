"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        new_head = Node(head.val)
        new = new_head
        original = head

        #First round: copy the list, original.random = new, new.random = original.random
        while new:
            new.random, original.random = original.random, new
            if original.next:
                new.next = Node(original.next.val)

            new = new.next
            original = original.next

        #Second round: update the random pointer to point to the new node
        node = new_head
        while node:
            if node.random:
                node.random = node.random.random
            node = node.next

        return new_head
        