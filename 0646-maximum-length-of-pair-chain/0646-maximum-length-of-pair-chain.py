class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key=lambda pair: pair[1])

        length = 0
        current_end = float('-inf')

        for left, right in pairs:
            if left > current_end:
                length += 1
                current_end = right

        return length
