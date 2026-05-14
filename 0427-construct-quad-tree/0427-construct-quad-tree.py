"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def construct_node(row, col, length):
            if length == 1:
                return Node(grid[row][col] == 1, True, None, None, None, None)

            mid = length // 2

            topLeft = construct_node(row - mid, col - mid, mid)
            topRight = construct_node(row - mid, col, mid)
            bottomLeft = construct_node(row, col - mid, mid)
            bottomRight = construct_node(row, col, mid)

            if all(node.isLeaf and node.val == topLeft.val for node in [topLeft, topRight, bottomLeft, bottomRight]):
                return Node(topLeft.val, True, None, None, None, None)

            else:
                return Node(topLeft.val, False, topLeft, topRight, bottomLeft, bottomRight)

        n = len(grid)
        return construct_node(n - 1, n - 1, n)
