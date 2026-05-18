class Solution:
    def findNthDigit(self, n: int) -> int:
        base = 1
        digits = 0
        power = 1

        while digits + (base * power * 9) < n:
            digits += base * power * 9
            power += 1
            base *= 10

        number = ((n - digits - 1) // power) + base
        s = str(number)
        return int(s[(n - digits - 1) % power])
        