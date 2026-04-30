class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left_head = left_tail = right_head = right_tail = None
        node = head

        while node:
            if node.val < x:
                if left_tail:
                    left_tail.next = node
                    left_tail = node
                else:
                    left_head = left_tail = node

            else:
                if right_tail:
                    right_tail.next = node
                    right_tail = node
                else:
                    right_head = right_tail = node

            node = node.next

        if left_head:
            head = left_head
            left_tail.next = right_head
        else:
            head = right_head

        if right_tail:
            right_tail.next = None
        elif left_tail:
            left_tail.next = None

        return head
        