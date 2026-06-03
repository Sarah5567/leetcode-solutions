class Solution:
    def makeIntegerBeautiful(self, n: int, target: int) -> int:
        x = 0
        power = 1
        sum_digits = sum(int(d) for d in str(n))

        while sum_digits > target:
            digit = n % 10

            if digit:
                addition = 10 - digit
                n += addition
                x += addition * power

            power *= 10
            n //= 10
            sum_digits = sum(int(d) for d in str(n))

        return x
