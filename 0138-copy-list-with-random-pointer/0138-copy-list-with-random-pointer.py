class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        new_head = Node(head.val)
        new = new_head
        original = head

        #First pass: copy the list
        while new:
            new.random, original.random = original.random, new
            if original.next:
                new.next = Node(original.next.val)

            new = new.next
            original = original.next

        #Second pass: update the random pointers to point to the corresponding new nodes
        node = new_head
        while node:
            if node.random:
                node.random = node.random.random
            node = node.next

        return new_head
        