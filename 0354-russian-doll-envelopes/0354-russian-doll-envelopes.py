class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda envelope: (envelope[0], -envelope[1]))
        tails = [float('inf')] * len(envelopes)
        k = 0

        for w, h in envelopes:
                index = bisect_left(tails, h)
                tails[index] = h
                if index + 1 >= k:
                    k = index + 1

        return k
