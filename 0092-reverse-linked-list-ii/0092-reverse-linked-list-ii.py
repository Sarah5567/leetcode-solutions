class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head

        if left == 1:
            before, first = None, head
        else:
            before = head
            for _ in range(left - 2):
                before = before.next
            first = before.next

        cur = first
        next_node = first.next

        for _ in range(left, right):
            prev, cur = cur, next_node
            next_node = cur.next
            cur.next = prev

        if before:
            before.next = cur
        else:
            head = cur

        first.next = next_node

        return head
