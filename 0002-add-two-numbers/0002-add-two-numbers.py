class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode((l1.val + l2.val) % 10)
        c = (l1.val + l2.val) // 10
        n1 = l1.next
        n2 = l2.next
        new_node = head

        while n1 or n2 or c:
            total = c + (n1.val if n1 else 0) + (n2.val if n2 else 0)
            new_node.next = ListNode((total) % 10)
            c = (total) // 10

            n1 = n1.next if n1 else None
            n2 = n2.next if n2 else None
            new_node = new_node.next

        return head
