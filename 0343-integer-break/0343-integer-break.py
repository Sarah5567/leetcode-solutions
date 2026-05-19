class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n - 1

        product = pow(3, n // 3)
        if n % 3 == 1:
            product *= 4 / 3
        elif n % 3 == 2:
            product *= 2

        return int(product)
