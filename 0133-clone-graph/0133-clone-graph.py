"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        nodes = {}

        def dfs(node):
            new_node = Node(node.val)
            nodes[node] = new_node

            for neighbor in node.neighbors:
                if neighbor not in nodes:
                    dfs(neighbor)
                new_node.neighbors.append(nodes[neighbor])

        dfs(node)
        return nodes[node]
            