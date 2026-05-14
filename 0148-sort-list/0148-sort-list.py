class Solution:

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        length = 0
        node = head
        while node:
            length += 1
            node = node.next

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

            while left_node and right_node:
                if left_node.val < right_node.val:
                    cur_node.next = left_node
                    left_node = left_node.next
                else:
                    cur_node.next = right_node
                    right_node = right_node.next
                cur_node = cur_node.next

            cur_node.next = left_node or right_node

            return head, next_node

        head, _ = merge_sort(head, 0, length - 1)
        return head