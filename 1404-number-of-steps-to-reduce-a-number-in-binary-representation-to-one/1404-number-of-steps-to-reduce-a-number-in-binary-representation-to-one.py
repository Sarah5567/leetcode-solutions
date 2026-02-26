class Solution:
    def numSteps(self, s: str) -> int:
        steps = 0
        carry = 0

        for bit in reversed(s[1:]):
            b = int(bit)

            if b + carry == 1:
                steps += 2
                carry = 1
            else:
                steps += 1

        return steps + carry
