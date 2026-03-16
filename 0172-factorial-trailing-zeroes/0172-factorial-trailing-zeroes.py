class Solution:
    def trailingZeroes(self, n: int) -> int:
        trailing_zeroes = 0
        five_factor = 5
        
        while five_factor <= n:
            trailing_zeroes += n // five_factor
            five_factor *= 5
        
        return trailing_zeroes
