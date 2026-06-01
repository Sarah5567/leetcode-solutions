class Solution:
    def numberOfWays(self, startPos, endPos, k):
        MOD = 10**9 + 7
        d = abs(endPos - startPos)

        if d > k or (k - d) % 2 != 0:
            return 0

        r = (k + d) // 2

        return comb(k, r) % MOD
        