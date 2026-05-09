class Solution:
    def myPow(self, x: float, n: int) -> float:
        cur_pow = x if n > 0 else 1 / x
        n = abs(n)
        ans = 1

        while n:
            if n & 1:
                ans *= cur_pow
            n = n >> 1
            cur_pow *= cur_pow

        return ans
