class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        q = deque()

        q.append(root)
        q.append(None)

        while len(q) > 1:
            node = q.popleft()
            if node:
                node.next = q[0]
                q.append(node.left)
                q.append(node.right)
            elif q[-1]:
                    q.append(None)

        return root
