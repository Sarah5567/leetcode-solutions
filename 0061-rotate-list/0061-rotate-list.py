# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def get_edges(node, n):
            if not node.next:
                nonlocal k
                k = k % n
                return node, None, n
            
            else:
                last, prev, total_n = get_edges(node.next, n + 1)
                if n == total_n - k:
                    prev = node

                return last, prev, total_n

        if not head or not k:
            return head

        last, prev, _ = get_edges(head, 1)
        if prev:
            last.next = head
            head = prev.next
            prev.next = None

        return head

