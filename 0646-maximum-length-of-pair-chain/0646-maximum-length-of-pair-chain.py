class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda pair: pair[1])

        length = 0
        edge = float('-inf')

        for left, right in pairs:
            if left > edge:
                length += 1
                edge = right

        return length
