# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head = ListNode()
        node = head.next
        new_node = new_head

        while True:
            if node.val != 0:
                new_node.val += node.val
            elif node.next:
                new_node.next = ListNode()
                new_node = new_node.next
            else:
                break
            
            node = node.next

        return new_head
