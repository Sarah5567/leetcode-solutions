# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse_one_group(self, node : Optional[ListNode], k : int, i : int) -> Tuple[ListNode, ListNode]:
        if i == k:
            return (node, node.next)
        else:
            first, last = self.reverse_one_group(node.next, k, i + 1)
            node.next.next = node
            return first, last

    def has_k_nodes(self, node : ListNode, k : int) -> bool:
        for _ in range(k):
            if not node:
                return False
            node = node.next
        return True

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not self.has_k_nodes(head, k):
            return head

        first, last = self.reverse_one_group(head, k, 1)
        head.next = last
        prev = head
        head = first

        while self.has_k_nodes(last, k):
            first, last = self.reverse_one_group(last, k, 1)
            prev.next.next = last

            cur_tail = prev.next
            prev.next = first
            prev = cur_tail


        return head
