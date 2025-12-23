# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_one_group(self, node : Optional[ListNode], k : int, i : int) -> Tuple[ListNode, ListNode]:
        if i == k:
            return (node, node.next)
        if not node.next:
            return (None, None)
        else:
            first, last = self.reverse_one_group(node.next, k, i + 1)
            if first:
                node.next.next = node
            return first, last

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        first, last = self.reverse_one_group(head, k, 1)
        head.next = last
        prev = head
        head = first

        while last:
            first, last = self.reverse_one_group(last, k, 1)
            if first:
                prev.next.next = last

                cur_tail = prev.next
                prev.next = first
                prev = cur_tail

        return head
