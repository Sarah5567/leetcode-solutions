class Solution:
    def reverse_one_group(self, node, k):
        if not node:
            return None, None
        if k == 1:
            return node, node.next

        first, last = self.reverse_one_group(node.next, k - 1)
        if not first:
            return None, None

        node.next.next = node
        return first, last

    def reverseKGroup(self, head, k):
        first, last = self.reverse_one_group(head, k)
        if not first:
            return head

        head.next = last
        prev = head
        head = first

        while True:
            first, last = self.reverse_one_group(last, k)
            if not first:
                break

            tail = prev.next
            tail.next = last
            prev.next = first
            prev = tail

        return head
