# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node = head
        length = 0
        while node:
            length += 1
            node = node.next

        if length == n:
            return head.next

        prev = head
        for _ in range(1, length - n):
            prev = prev.next

        prev.next = prev.next.next
        return head
        