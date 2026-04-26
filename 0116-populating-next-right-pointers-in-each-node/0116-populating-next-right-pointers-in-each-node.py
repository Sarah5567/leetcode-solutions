class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = deque()
        q.append(root)
        prev = 0

        while q[0]:
            size = max(1, prev * 2)
            for _ in range(size):
                node = q.popleft()
                q.append(node.left)
                q.append(node.right)
                node.next = q[0]

            node.next = None
            prev = size

        return root
