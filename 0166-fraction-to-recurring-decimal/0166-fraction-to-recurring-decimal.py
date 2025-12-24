class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        res = []

        # sign
        if (numerator < 0) ^ (denominator < 0):
            res.append('-')

        numerator, denominator = abs(numerator), abs(denominator)

        # integer part
        integer = numerator // denominator
        res.append(str(integer))

        remainder = numerator % denominator
        if remainder == 0:
            return ''.join(res)

        res.append('.')

        # map remainder -> index in result
        seen = {}

        while remainder:
            if remainder in seen:
                idx = seen[remainder]
                res.insert(idx, '(')
                res.append(')')
                break

            seen[remainder] = len(res)

            remainder *= 10
            res.append(str(remainder // denominator))
            remainder %= denominator

        return ''.join(res)
