# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        node = head
        while node:
            length += 1
            node = node.next

        if not length:
            return None

        def merge_sort(node, left, right):
            if left == right:
                next_node = node.next
                node.next = None
                return node, next_node

            mid = left + (right - left) // 2
            left_head, next_node = merge_sort(node, left, mid)
            right_head, next_node = merge_sort(next_node, mid + 1, right)

            left_node = left_head
            right_node = right_head
            if left_node.val < right_node.val:
                head = left_node
                left_node = left_node.next
            else:
                head = right_node
                right_node = right_node.next

            cur_node = head

            for i in range(left, right):
                if not right_node or (left_node and left_node.val < right_node.val):
                    cur_node.next = left_node
                    left_node = left_node.next
                else:
                    cur_node.next = right_node
                    right_node = right_node.next
                cur_node = cur_node.next

            return head, next_node

        head, _ = merge_sort(head, 0, length - 1)
        node = head
        for _ in range(length - 1):
            node = node.next
        node.next = None

        return head
